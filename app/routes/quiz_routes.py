"""
퀴즈 관련 라우트 정의
"""
from flask import Blueprint, render_template, request, redirect, url_for, session, abort
from app.models.quiz_data import (
    get_quiz_data, 
    get_quiz_subjects, 
    get_all_questions,
    get_subject_name
)
from app.config import Config
import random
from datetime import datetime

# 블루프린트 생성
quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/', methods=['GET', 'POST'])
def index():
    """메인 페이지"""
    if request.method == "POST":
        subject = request.form.get("subject")
        if subject not in [s["code"] for s in get_quiz_subjects()]:
            # 유효하지 않은 과목인 경우
            return redirect(url_for('quiz.index'))
        return redirect(url_for('quiz.quiz', subject=subject))
    
    # 최근 점수 기록
    recent_scores = session.get('recent_scores', [])
    subjects = get_quiz_subjects()
    
    return render_template('index.html', 
                          recent_scores=recent_scores,
                          subjects=subjects)

@quiz_bp.route('/quiz/<subject>', methods=['GET', 'POST'])
def quiz(subject):
    """퀴즈 페이지"""
    try:
        # 유효한 과목인지 확인
        if subject != "ALL" and subject not in get_quiz_data().keys():
            return redirect(url_for('quiz.index'))
        
        # 과목에 따른 문제 가져오기
        if subject == "ALL":
            questions = get_all_questions()
        else:
            questions = get_quiz_data(subject)
            if not questions:
                return redirect(url_for('quiz.index'))
        
        if request.method == "POST":
            print("POST 요청 받음: ", request.form)
            score = 0
            results = []
            
            for idx, q in enumerate(questions):
                # 수정된 name 형식에 맞춰 데이터 가져오기
                question_key = f"question_{subject}_{idx}"
                user_answer = request.form.get(question_key)
                print(f"문항 {idx}의 사용자 응답 체크: {question_key} = {user_answer}")
                is_answered = user_answer is not None
                correct = int(user_answer) == q['answer'] if is_answered else False
                
                if correct:
                    score += 1
                    
                results.append({
                    'question': q['question'],
                    'user_answer': int(user_answer) if is_answered else None,
                    'user_answer_text': q['options'][int(user_answer)] if is_answered else "무응답",
                    'correct_answer': q['answer'],
                    'correct_answer_text': q['options'][q['answer']],
                    'is_correct': correct,
                    'is_answered': is_answered,
                    'explanation': q['explanation'],
                    'all_options': q['options']
                })
            
            # 백분율 계산
            percentage = int((score / len(questions)) * 100) if questions else 0
            
            # 시험 결과 저장
            recent_scores = session.get('recent_scores', [])
            recent_scores.append({
                'subject': subject,
                'subject_name': get_subject_name(subject),
                'score': score,
                'total': len(questions),
                'percentage': percentage,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            
            # 최근 N개 결과만 유지
            recent_scores = recent_scores[-Config.MAX_RECENT_SCORES:]
            session['recent_scores'] = recent_scores
            
            return render_template('result.html', 
                                  score=score, 
                                  total=len(questions), 
                                  results=results, 
                                  percentage=percentage,
                                  subject=subject,
                                  subject_name=get_subject_name(subject))
        
        # GET 요청 - 문제 출제
        # 문제 순서 섞기
        random.shuffle(questions)
        return render_template('quiz.html', 
                              questions=questions, 
                              subject=subject,
                              subject_name=get_subject_name(subject),
                              quiz_time=Config.QUIZ_TIME)
    except Exception as e:
        # 오류 로깅
        print(f"Error in quiz route: {e}")
        # 사용자에게 오류 페이지 표시 또는 인덱스로 리다이렉트
        return redirect(url_for('quiz.index'))

@quiz_bp.errorhandler(404)
def page_not_found(e):
    """404 오류 처리"""
    return render_template('404.html'), 404

@quiz_bp.errorhandler(500)
def internal_server_error(e):
    """500 오류 처리"""
    return render_template('500.html'), 500

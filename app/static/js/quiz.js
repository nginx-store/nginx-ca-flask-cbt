/**
 * 퀴즈 관련 JavaScript 기능
 */

/**
 * 퀴즈 초기화 함수
 * @param {number} quizTime - 퀴즈 시간(초)
 * @param {string} subject - 퀴즈 과목 코드
 */
function initQuiz(quizTime, subject) {
    console.log("초기화 매개변수:", quizTime, subject);
    const timerElement = document.getElementById('timer');
    const timerBar = document.getElementById('timer-bar');
    const quizForm = document.getElementById('quiz-form');
    console.log("퀴즈 폼 필드:", quizForm);
    let timeLeft = quizTime;
    let timerInterval;

    // 타이머 업데이트 함수
    function updateTimer() {
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        
        timerElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        timerBar.style.width = `${(timeLeft / quizTime) * 100}%`;
        
        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            document.getElementById('quiz-form').submit();
        }
        
        timeLeft--;
    }
    
    updateTimer();
    timerInterval = setInterval(updateTimer, 1000);

    // 페이지 언로드 시 타이머 정리
    window.addEventListener('beforeunload', function() {
        clearInterval(timerInterval);
    });
    
    // 문제별 라디오 버튼 관리
    const questions = document.querySelectorAll('.question');
    
    // 각 문제별로 라디오 버튼 이벤트 처리
    questions.forEach((question, questionIndex) => {
        // 현재 문제의 모든 라디오 버튼
        const radioName = `question_${subject}_${questionIndex}`;
        const radioButtons = question.querySelectorAll(`input[name="${radioName}"]`);
        
        radioButtons.forEach(radio => {
            radio.addEventListener('change', function() {
                // 현재 문제에 속한 모든 라벨
                const labels = question.querySelectorAll('label.option-label');
                
                // 모든 라벨 스타일 초기화 후 선택된 것만 강조
                labels.forEach(label => {
                    if (label.getAttribute('for') === this.id) {
                        // 선택된 라디오 버튼의 라벨 강조
                        label.style.fontWeight = '600';
                        label.style.borderLeft = '5px solid #009639';
                    } else {
                        // 다른 라벨은 스타일 초기화
                        label.style.fontWeight = 'normal';
                        label.style.borderLeft = 'none';
                    }
                });
            });
        });
    });
    
    // 폼 제출 시 검증
    console.log("폼 제출 이벤트 리스너 추가 중");
    quizForm.addEventListener('submit', function(e) {
        console.log("폼 제출 이벤트 발생");
        e.preventDefault();
        
        // 모든 문항이 선택되었는지 확인
        const totalQuestions = questions.length;
        let answeredQuestions = 0;
        let firstUnansweredIndex = -1;
        
        // 각 문제별로 답변 여부 확인
        questions.forEach((question, idx) => {
            // 현재 subject와 idx에 해당하는 라디오 버튼 그룹 찾기
            const radioName = `question_${subject}_${idx}`;
            const radioButtons = question.querySelectorAll(`input[name="${radioName}"]`);
            let isAnswered = false;
            
            // 현재 문제에 하나라도 체크된 라디오 버튼이 있는지 확인
            radioButtons.forEach(radio => {
                if (radio.checked) {
                    isAnswered = true;
                }
            });
            
            if (isAnswered) {
                answeredQuestions++;
                question.style.borderLeft = '5px solid #28a745';
            } else {
                question.style.borderLeft = '5px solid #dc3545';
                if (firstUnansweredIndex === -1) {
                    firstUnansweredIndex = idx;
                }
            }
        });
        
        // 모든 문항이 답변되었는지 확인
        if (answeredQuestions < totalQuestions) {
            alert(`총 ${totalQuestions}개의 문항 중 ${answeredQuestions}개만 답변했습니다.\n모든 문항에 답변해주세요.`);
            
            // 첫 번째 미답변 문항으로 스크롤
            if (firstUnansweredIndex !== -1) {
                const firstUnansweredQuestion = document.getElementById(`question-${subject}-${firstUnansweredIndex}`);
                if (firstUnansweredQuestion) {
                    firstUnansweredQuestion.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
            
            return false;
        }
        
        // 모든 검증 통과, 폼 제출
        quizForm.submit();
    });
}

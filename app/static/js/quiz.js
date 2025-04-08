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
    let formSubmitted = false; // 폼 제출 상태를 추적

    // 다중 응답 화면일 경우 진행상황 표시에 사용할 요소 참조
    const answerProgressBar = document.getElementById('answer-progress');
    const progressText = document.getElementById('progress-text');

    // HTML5 required 속성 사용 중지 - 아래에서 수동으로 검증
    // 이것이 "not focusable" 오류를 해결합니다
    const allRadios = document.querySelectorAll('input[type="radio"]');
    allRadios.forEach(radio => {
        radio.removeAttribute('required');
    });

    // 타이머 업데이트 함수
    function updateTimer() {
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        
        timerElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        timerBar.style.width = `${(timeLeft / quizTime) * 100}%`;
        
        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            if (!formSubmitted) {
                formSubmitted = true;
                showMessage('시간이 다 되었습니다. 퀴즈가 자동으로 제출됩니다.', 'warning');
                submitForm();
            }
        }
        
        timeLeft--;
    }
    
    updateTimer();
    timerInterval = setInterval(updateTimer, 1000);

    // 페이지 언로드 시 타이머 정리
    window.addEventListener('beforeunload', function(e) {
        clearInterval(timerInterval);
        
        // 폼이 제출되지 않았고 답변이 있는 경우 경고 표시
        if (!formSubmitted && hasAnyAnswers()) {
            e.preventDefault();
            e.returnValue = '응답한 내용이 있습니다. 정말로 페이지를 떠나시겠습니까?';
            return e.returnValue;
        }
    });
    
    // 사용자가 어떤 문제라도 답변했는지 확인
    function hasAnyAnswers() {
        const radioButtons = document.querySelectorAll('input[type="radio"]:checked');
        return radioButtons.length > 0;
    }

    // 진행상황 표시 함수
    function updateProgressBar() {
        const totalQuestions = document.querySelectorAll('.question').length;
        const answeredQuestions = document.querySelectorAll('input[type="radio"]:checked').length;
        const percentage = (answeredQuestions / totalQuestions) * 100;
        
        if (answerProgressBar) {
            answerProgressBar.style.width = `${percentage}%`;
            answerProgressBar.setAttribute('aria-valuenow', percentage);
        }
        
        if (progressText) {
            progressText.textContent = `응답 진행률: ${answeredQuestions}/${totalQuestions}`;
        }
    }
    
    // 문제별 라디오 버튼 관리
    const questions = document.querySelectorAll('.question');
    
    // 각 문제별로 라디오 버튼 이벤트 처리
    questions.forEach((question, questionIndex) => {
        // 현재 문제의 모든 라디오 버튼
        const radioName = `question_${subject}_${questionIndex}`;
        const radioButtons = question.querySelectorAll(`input[name="${radioName}"]`);
        
        // 알림 변경
        const statusBadge = question.querySelector('.question-status');
        
        radioButtons.forEach(radio => {
            radio.addEventListener('change', function() {
                // 현재 문제에 속한 모든 라벨
                const labels = question.querySelectorAll('label.option-label');
                
                // 문제 상태 표시 업데이트
                if (statusBadge) {
                    statusBadge.textContent = '응답함';
                    statusBadge.classList.remove('bg-secondary');
                    statusBadge.classList.add('bg-success');
                }
                
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
                
                // 진행상황 업데이트
                updateProgressBar();
            });
        });
    });
    
    // 초기 진행상황 설정
    updateProgressBar();
    
    // 메시지 표시 함수
    function showMessage(message, type = 'danger') {
        // 이미 존재하는 메시지 제거
        const existingMessage = document.getElementById('error-message');
        if (existingMessage) {
            existingMessage.remove();
        }
        
        // 메시지 컨테이너 생성
        const messageContainer = document.createElement('div');
        messageContainer.id = 'error-message';
        messageContainer.className = `alert alert-${type} alert-dismissible fade show`;
        messageContainer.setAttribute('role', 'alert');
        messageContainer.style.position = 'fixed';
        messageContainer.style.top = '20px';
        messageContainer.style.left = '50%';
        messageContainer.style.transform = 'translateX(-50%)';
        messageContainer.style.zIndex = '9999';
        messageContainer.style.maxWidth = '80%';
        messageContainer.style.boxShadow = '0 4px 8px rgba(0,0,0,0.1)';
        
        // 메시지 내용
        messageContainer.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        
        // 페이지에 메시지 추가
        document.body.appendChild(messageContainer);
        
        // 5초 후 자동으로 닫히도록 설정
        setTimeout(() => {
            const alertElement = bootstrap.Alert.getOrCreateInstance(messageContainer);
            if (alertElement) alertElement.close();
        }, 5000);
    }
    
    // 폼 제출 함수
    function submitForm() {
        formSubmitted = true;
        // HTML 폼을 제출하기 전에 폼 유효성 검사를 위해 수동으로 제출 처리
        quizForm.submit();
    }
    
    // 폼 제출 시 검증
    console.log("폼 제출 이벤트 리스너 추가 중");
    quizForm.addEventListener('submit', function(e) {
        console.log("폼 제출 이벤트 발생");
        e.preventDefault();
        
        // 모든 문항이 선택되었는지 확인
        const totalQuestions = questions.length;
        let answeredQuestions = 0;
        let unansweredQuestions = [];
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
                unansweredQuestions.push(idx + 1); // 문제 번호는 1부터 시작
                if (firstUnansweredIndex === -1) {
                    firstUnansweredIndex = idx;
                }
            }
        });
        
        // 모든 문항이 답변되었는지 확인
        if (answeredQuestions < totalQuestions) {
            const remainingQuestions = totalQuestions - answeredQuestions;
            const unansweredList = unansweredQuestions.join(', ');
            
            showMessage(`
                <strong>미응답 문항이 있습니다!</strong><br>
                총 ${totalQuestions}개의 문항 중 ${answeredQuestions}개만 답변했습니다.<br>
                미응답 문항: <span class="badge bg-warning text-dark">${unansweredList}</span><br>
                모든 문항에 답변해주세요.
            `, 'danger');
            
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
        submitForm();
    });
}
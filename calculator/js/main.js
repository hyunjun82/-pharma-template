// 검색 기능
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');

    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase().trim();

            // 모든 계산기 카드 가져오기
            const calcCards = document.querySelectorAll('.calc-card');
            const categories = document.querySelectorAll('.calculator-category');

            if (searchTerm === '') {
                // 검색어가 없으면 모두 표시
                calcCards.forEach(card => card.style.display = 'block');
                categories.forEach(category => category.style.display = 'block');
                return;
            }

            // 각 카테고리별로 검색
            categories.forEach(category => {
                const cardsInCategory = category.querySelectorAll('.calc-card');
                let hasVisibleCard = false;

                cardsInCategory.forEach(card => {
                    const title = card.querySelector('h3').textContent.toLowerCase();
                    const description = card.querySelector('p').textContent.toLowerCase();

                    if (title.includes(searchTerm) || description.includes(searchTerm)) {
                        card.style.display = 'block';
                        hasVisibleCard = true;

                        // 검색어 하이라이트
                        highlightText(card, searchTerm);
                    } else {
                        card.style.display = 'none';
                    }
                });

                // 카테고리에 보이는 카드가 없으면 카테고리도 숨김
                if (hasVisibleCard) {
                    category.style.display = 'block';
                } else {
                    category.style.display = 'none';
                }
            });
        });
    }

    // 검색어 하이라이트 함수
    function highlightText(element, searchTerm) {
        // 기존 하이라이트 제거
        const highlighted = element.querySelectorAll('.highlight');
        highlighted.forEach(el => {
            el.classList.remove('highlight');
        });

        // 새 하이라이트 추가 (필요시 CSS 추가)
        element.style.animation = 'none';
        setTimeout(() => {
            element.style.animation = 'fadeIn 0.3s ease-out';
        }, 10);
    }

    // 부드러운 스크롤
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // 스크롤 시 헤더 그림자 효과
    let lastScroll = 0;
    const header = document.querySelector('.main-header');

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 100) {
            header.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
        } else {
            header.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
        }

        lastScroll = currentScroll;
    });

    // 계산기 카드 클릭 이벤트 (Google Analytics 추적용)
    document.querySelectorAll('.calc-card').forEach(card => {
        card.addEventListener('click', function(e) {
            const calcName = this.querySelector('h3').textContent;

            // Google Analytics 이벤트 전송 (GA4)
            if (typeof gtag !== 'undefined') {
                gtag('event', 'calculator_click', {
                    'calculator_name': calcName,
                    'event_category': 'engagement',
                    'event_label': calcName
                });
            }

            // 콘솔에 로그 (개발용)
            console.log('Calculator clicked:', calcName);
        });
    });

    // 인기 계산기 카운트 애니메이션 (선택사항)
    function animateValue(element, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const value = Math.floor(progress * (end - start) + start);
            element.textContent = value.toLocaleString('ko-KR');
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }

    // Intersection Observer로 화면에 보일 때 애니메이션
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // 모든 카테고리 섹션 관찰
    document.querySelectorAll('.calculator-category').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });

    // 모바일 터치 제스처 개선
    let touchStartY = 0;
    let touchEndY = 0;

    document.addEventListener('touchstart', function(e) {
        touchStartY = e.changedTouches[0].screenY;
    }, false);

    document.addEventListener('touchend', function(e) {
        touchEndY = e.changedTouches[0].screenY;
        handleSwipe();
    }, false);

    function handleSwipe() {
        // 위로 스와이프 감지 등 추가 기능 구현 가능
        const swipeDistance = touchStartY - touchEndY;
        if (Math.abs(swipeDistance) > 100) {
            // 스와이프 이벤트 처리
        }
    }

    // 페이지 로드 완료 후 애드센스 최적화
    window.addEventListener('load', function() {
        // 광고 가시성 추적
        const adContainers = document.querySelectorAll('.ad-container');

        adContainers.forEach(ad => {
            const adObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        // 광고가 화면에 보이면 로그
                        console.log('Ad visible:', entry.target.className);

                        // Google Analytics에 광고 노출 기록
                        if (typeof gtag !== 'undefined') {
                            gtag('event', 'ad_impression', {
                                'ad_position': entry.target.className
                            });
                        }
                    }
                });
            }, { threshold: 0.5 });

            adObserver.observe(ad);
        });
    });
});

// 키보드 단축키 (선택사항)
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K로 검색창 포커스
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            searchInput.focus();
        }
    }

    // ESC로 검색 초기화
    if (e.key === 'Escape') {
        const searchInput = document.getElementById('searchInput');
        if (searchInput && searchInput.value) {
            searchInput.value = '';
            searchInput.dispatchEvent(new Event('input'));
        }
    }
});

// 로컬 스토리지로 최근 본 계산기 저장
function saveRecentCalculator(calcName) {
    let recent = JSON.parse(localStorage.getItem('recentCalculators') || '[]');

    // 중복 제거
    recent = recent.filter(item => item !== calcName);

    // 맨 앞에 추가
    recent.unshift(calcName);

    // 최대 10개만 저장
    recent = recent.slice(0, 10);

    localStorage.setItem('recentCalculators', JSON.stringify(recent));
}

// 최근 본 계산기 표시 (선택사항 - UI에 추가 필요)
function getRecentCalculators() {
    return JSON.parse(localStorage.getItem('recentCalculators') || '[]');
}

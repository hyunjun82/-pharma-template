import { useState } from 'react'
import { Link } from 'react-router-dom'

const categories = [
  {
    id: 'realestate',
    title: '부동산',
    icon: '🏠',
    calculators: [
      { name: '취득세 계산기', url: '/realestate/acquisition-tax', popular: true, implemented: true },
      { name: '양도소득세 계산기', url: '/realestate/transfer-tax' },
      { name: '종합부동산세 계산기', url: '/realestate/comprehensive-tax' },
      { name: '재산세 계산기', url: '/realestate/property-tax' },
      { name: '전세대출 계산기', url: '/realestate/jeonse-loan' },
      { name: '주택담보대출 계산기', url: '/realestate/mortgage-loan' },
      { name: '중개수수료 계산기', url: '/realestate/brokerage-fee' },
      { name: '평수 계산기', url: '/realestate/pyeong-converter', implemented: true },
    ],
  },
  {
    id: 'salary',
    title: '급여/세금',
    icon: '💰',
    calculators: [
      { name: '연봉 실수령액 계산기', url: '/salary/take-home-pay', popular: true, implemented: true },
      { name: '퇴직금 계산기', url: '/salary/severance-pay' },
      { name: '4대보험료 계산기', url: '/salary/social-insurance' },
      { name: '연말정산 계산기', url: '/salary/year-end-tax' },
      { name: '근로소득세 계산기', url: '/salary/income-tax' },
      { name: '실업급여 계산기', url: '/salary/unemployment-benefit' },
      { name: '주휴수당 계산기', url: '/salary/weekly-holiday-pay' },
      { name: '시급 계산기', url: '/salary/hourly-wage' },
    ],
  },
  {
    id: 'loan',
    title: '대출/금융',
    icon: '🏦',
    calculators: [
      { name: '대출이자 계산기', url: '/loan/interest', popular: true, implemented: true },
      { name: '대출상환 계산기', url: '/loan/repayment' },
      { name: '적금 계산기', url: '/finance/savings' },
      { name: '예금이자 계산기', url: '/finance/deposit-interest' },
      { name: '복리 계산기', url: '/finance/compound-interest' },
    ],
  },
  {
    id: 'car',
    title: '자동차',
    icon: '🚗',
    calculators: [
      { name: '자동차 취득세 계산기', url: '/car/acquisition-tax' },
      { name: '자동차세 계산기', url: '/car/automobile-tax' },
      { name: '자동차 할부금융 계산기', url: '/car/installment' },
    ],
  },
  {
    id: 'stock',
    title: '주식/투자',
    icon: '📈',
    calculators: [
      { name: '주식 평균단가 계산기', url: '/stock/average-price' },
      { name: '주식 수익률 계산기', url: '/stock/return-rate' },
      { name: '주식 수수료 계산기', url: '/stock/commission' },
      { name: '배당금 계산기', url: '/stock/dividend' },
    ],
  },
  {
    id: 'life',
    title: '생활/건강',
    icon: '💊',
    calculators: [
      { name: 'BMI 계산기', url: '/health/bmi', popular: true, implemented: true },
      { name: '기초대사량 계산기', url: '/health/bmr' },
      { name: '만나이 계산기', url: '/life/korean-age' },
      { name: 'D-Day 계산기', url: '/life/d-day' },
      { name: '환율 계산기', url: '/life/exchange-rate' },
      { name: '부가세 계산기', url: '/life/vat' },
    ],
  },
  {
    id: 'pregnancy',
    title: '임신/출산',
    icon: '👶',
    calculators: [
      { name: '출산예정일 계산기', url: '/pregnancy/due-date' },
      { name: '배란일 계산기', url: '/pregnancy/ovulation' },
      { name: '육아휴직급여 계산기', url: '/pregnancy/parental-leave' },
    ],
  },
  {
    id: 'pension',
    title: '연금/보험',
    icon: '🛡️',
    calculators: [
      { name: '국민연금 계산기', url: '/pension/national-pension' },
      { name: '건강보험료 계산기', url: '/insurance/health-insurance' },
    ],
  },
  {
    id: 'business',
    title: '프리랜서/사업자',
    icon: '💼',
    calculators: [
      { name: '종합소득세 계산기', url: '/business/comprehensive-income' },
      { name: '부가가치세 계산기', url: '/business/vat' },
      { name: '3.3% 세금계산기', url: '/business/freelancer-tax' },
    ],
  },
  {
    id: 'education',
    title: '교육',
    icon: '🎓',
    calculators: [
      { name: '내신등급 계산기', url: '/education/school-grade' },
      { name: '학점(GPA) 계산기', url: '/education/gpa' },
    ],
  },
]

export default function Home() {
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedCategory, setSelectedCategory] = useState('all')

  const filteredCategories = categories
    .map(category => ({
      ...category,
      calculators: category.calculators.filter(calc =>
        calc.name.toLowerCase().includes(searchTerm.toLowerCase())
      ),
    }))
    .filter(category =>
      (selectedCategory === 'all' || category.id === selectedCategory) &&
      category.calculators.length > 0
    )

  const popularCalculators = categories
    .flatMap(cat => cat.calculators.filter(calc => calc.popular))
    .slice(0, 4)

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-white">
      {/* Header */}
      <header className="border-b border-gray-200 bg-white/80 backdrop-blur-lg sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <Link to="/" className="flex items-center space-x-3">
              <div className="text-2xl">🧮</div>
              <h1 className="text-xl font-semibold text-gray-900">계산기</h1>
            </Link>
            <nav className="hidden md:flex space-x-8">
              <Link to="/" className="text-sm font-medium text-gray-700 hover:text-gray-900">
                홈
              </Link>
              <a href="#" className="text-sm font-medium text-gray-700 hover:text-gray-900">
                가이드
              </a>
              <a href="#" className="text-sm font-medium text-gray-700 hover:text-gray-900">
                문의
              </a>
            </nav>
          </div>
        </div>
      </header>

      {/* Hero */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-16 pb-12">
        <div className="text-center max-w-3xl mx-auto">
          <h2 className="text-5xl font-bold text-gray-900 mb-4">
            필요한 계산,
            <br />
            <span className="bg-gradient-to-r from-blue-600 to-cyan-500 bg-clip-text text-transparent">
              빠르고 정확하게
            </span>
          </h2>
          <p className="text-xl text-gray-600 mb-8">
            부동산부터 급여까지, 모든 계산기를 한곳에서
          </p>

          {/* Search */}
          <div className="relative max-w-2xl mx-auto">
            <input
              type="text"
              placeholder="계산기를 검색하세요 (예: 취득세, 실수령액, BMI)"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full px-6 py-4 text-lg border border-gray-300 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent shadow-sm"
            />
            <div className="absolute right-4 top-1/2 transform -translate-y-1/2 text-gray-400">
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
          </div>
        </div>
      </section>

      {/* Popular */}
      {!searchTerm && (
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-12">
          <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-4">인기 계산기</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {popularCalculators.map((calc, idx) => (
              calc.implemented ? (
                <Link
                  key={idx}
                  to={calc.url}
                  className="group p-6 bg-white border border-gray-200 rounded-2xl hover:border-blue-300 hover:shadow-lg transition-all duration-200"
                >
                  <div className="flex items-center justify-between">
                    <span className="text-base font-medium text-gray-900 group-hover:text-blue-600">
                      {calc.name}
                    </span>
                    <svg className="w-5 h-5 text-gray-400 group-hover:text-blue-600 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                    </svg>
                  </div>
                </Link>
              ) : (
                <div
                  key={idx}
                  className="p-6 bg-gray-100 border border-gray-200 rounded-2xl opacity-60"
                >
                  <div className="flex items-center justify-between">
                    <span className="text-base font-medium text-gray-500">
                      {calc.name}
                      <span className="ml-2 text-xs">(준비중)</span>
                    </span>
                  </div>
                </div>
              )
            ))}
          </div>
        </section>
      )}

      {/* Category Filter */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-8">
        <div className="flex overflow-x-auto space-x-2 pb-2 scrollbar-hide">
          <button
            onClick={() => setSelectedCategory('all')}
            className={`px-4 py-2 rounded-full text-sm font-medium whitespace-nowrap transition-colors ${
              selectedCategory === 'all' ? 'bg-gray-900 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
            }`}
          >
            전체
          </button>
          {categories.map((cat) => (
            <button
              key={cat.id}
              onClick={() => setSelectedCategory(cat.id)}
              className={`px-4 py-2 rounded-full text-sm font-medium whitespace-nowrap transition-colors ${
                selectedCategory === cat.id ? 'bg-gray-900 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              {cat.icon} {cat.title}
            </button>
          ))}
        </div>
      </section>

      {/* Calculators */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20">
        {filteredCategories.length === 0 ? (
          <div className="text-center py-12">
            <div className="text-6xl mb-4">🔍</div>
            <p className="text-gray-500">검색 결과가 없습니다</p>
          </div>
        ) : (
          <div className="space-y-12">
            {filteredCategories.map((category) => (
              <div key={category.id}>
                <div className="flex items-center space-x-3 mb-6">
                  <span className="text-3xl">{category.icon}</span>
                  <h3 className="text-2xl font-bold text-gray-900">{category.title}</h3>
                  <span className="text-sm text-gray-500">({category.calculators.length})</span>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                  {category.calculators.map((calc, idx) => (
                    calc.implemented ? (
                      <Link
                        key={idx}
                        to={calc.url}
                        className="group relative p-5 bg-white border border-gray-200 rounded-xl hover:border-gray-300 hover:shadow-md transition-all duration-200"
                      >
                        {calc.popular && (
                          <span className="absolute top-3 right-3 px-2 py-1 bg-blue-50 text-blue-600 text-xs font-semibold rounded-full">
                            인기
                          </span>
                        )}
                        <div className="flex items-start justify-between">
                          <span className="text-sm font-medium text-gray-900 group-hover:text-blue-600 pr-8">
                            {calc.name}
                          </span>
                          <svg className="w-4 h-4 text-gray-400 group-hover:text-blue-600 transform group-hover:translate-x-0.5 transition-transform flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                          </svg>
                        </div>
                      </Link>
                    ) : (
                      <div
                        key={idx}
                        className="relative p-5 bg-gray-50 border border-gray-200 rounded-xl opacity-60"
                      >
                        <div className="flex items-start justify-between">
                          <span className="text-sm font-medium text-gray-500 pr-8">
                            {calc.name}
                            <span className="block text-xs mt-1">준비중</span>
                          </span>
                        </div>
                      </div>
                    )
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      {/* Footer */}
      <footer className="border-t border-gray-200 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="text-center">
            <div className="flex items-center justify-center space-x-2 mb-4">
              <span className="text-2xl">🧮</span>
              <span className="text-lg font-semibold">계산기</span>
            </div>
            <p className="text-sm text-gray-600 mb-4">
              필요한 모든 계산을 빠르고 정확하게
            </p>
            <p className="text-sm text-gray-500">© 2025 JJYU Calculator. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}

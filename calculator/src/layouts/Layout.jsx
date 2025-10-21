import { Link } from 'react-router-dom'

export default function Layout({ children }) {
  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-white flex flex-col">
      {/* Header */}
      <header className="border-b border-gray-200 bg-white/80 backdrop-blur-lg sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <Link to="/" className="flex items-center space-x-3 hover:opacity-80 transition">
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

      {/* Main Content */}
      <main className="flex-1">
        {children}
      </main>

      {/* Footer */}
      <footer className="border-t border-gray-200 bg-gray-50 mt-auto">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="text-center">
            <div className="flex items-center justify-center space-x-2 mb-2">
              <span className="text-xl">🧮</span>
              <span className="font-semibold">계산기</span>
            </div>
            <p className="text-sm text-gray-600">필요한 모든 계산을 빠르고 정확하게</p>
            <p className="text-xs text-gray-500 mt-2">© 2025 JJYU Calculator</p>
          </div>
        </div>
      </footer>
    </div>
  )
}

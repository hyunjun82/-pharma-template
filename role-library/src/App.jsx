import { useState, useEffect } from 'react'
import './App.css'

// 초기 샘플 데이터
const initialRoles = [
  {
    id: 1,
    title: '숏폼 썸네일 이미지',
    category: 'Image',
    prompt: 'Create a vibrant, eye-catching thumbnail for a short-form video about [TOPIC]. The image should feature bold text, dynamic composition, and attention-grabbing colors. Ultra HD, professional quality.',
    favorite: false,
  },
  {
    id: 2,
    title: 'YouTube 인트로 영상',
    category: 'Video',
    prompt: 'Generate a professional YouTube intro video with smooth transitions, modern typography, and energetic music. Duration: 5-10 seconds. Include channel name and logo space.',
    favorite: true,
  },
  {
    id: 3,
    title: '제품 홍보 이미지',
    category: 'Image',
    prompt: 'Professional product photography style image of [PRODUCT] on a clean white background. Studio lighting, high resolution, commercial quality, sharp focus.',
    favorite: false,
  },
  {
    id: 4,
    title: '릴스 배경 영상',
    category: 'Video',
    prompt: 'Create an abstract, looping background video perfect for Instagram Reels. Smooth motion, gradient colors, modern aesthetic. 9:16 aspect ratio, 15 seconds.',
    favorite: false,
  },
];

const categories = ['All', 'Image', 'Video', 'Animation'];

function App() {
  const [roles, setRoles] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [showAddModal, setShowAddModal] = useState(false);
  const [editingRole, setEditingRole] = useState(null);
  const [newRole, setNewRole] = useState({
    title: '',
    category: 'Image',
    prompt: '',
    favorite: false,
  });

  // LocalStorage에서 데이터 로드
  useEffect(() => {
    const saved = localStorage.getItem('roleLibrary');
    if (saved) {
      setRoles(JSON.parse(saved));
    } else {
      setRoles(initialRoles);
    }
  }, []);

  // LocalStorage에 데이터 저장
  useEffect(() => {
    if (roles.length > 0) {
      localStorage.setItem('roleLibrary', JSON.stringify(roles));
    }
  }, [roles]);

  // 필터링된 역할 목록
  const filteredRoles = roles.filter(role => {
    const matchesSearch = role.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         role.prompt.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCategory = selectedCategory === 'All' || role.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  // 역할 추가
  const handleAddRole = () => {
    if (newRole.title && newRole.prompt) {
      const role = {
        ...newRole,
        id: Date.now(),
      };
      setRoles([...roles, role]);
      setNewRole({ title: '', category: 'Image', prompt: '', favorite: false });
      setShowAddModal(false);
    }
  };

  // 역할 삭제
  const handleDeleteRole = (id) => {
    setRoles(roles.filter(role => role.id !== id));
  };

  // 즐겨찾기 토글
  const toggleFavorite = (id) => {
    setRoles(roles.map(role =>
      role.id === id ? { ...role, favorite: !role.favorite } : role
    ));
  };

  // 프롬프트 복사
  const copyPrompt = (prompt) => {
    navigator.clipboard.writeText(prompt);
    alert('프롬프트가 복사되었습니다!');
  };

  // 역할 편집
  const handleEditRole = (role) => {
    setEditingRole(role);
    setNewRole(role);
    setShowAddModal(true);
  };

  // 역할 업데이트
  const handleUpdateRole = () => {
    if (newRole.title && newRole.prompt) {
      setRoles(roles.map(role =>
        role.id === editingRole.id ? { ...newRole, id: role.id } : role
      ));
      setNewRole({ title: '', category: 'Image', prompt: '', favorite: false });
      setEditingRole(null);
      setShowAddModal(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <h1>🎬 Role Library</h1>
        <p>AI 프롬프트 템플릿 관리</p>
      </header>

      <div className="toolbar">
        <input
          type="text"
          placeholder="검색..."
          className="search-input"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />

        <div className="categories">
          {categories.map(cat => (
            <button
              key={cat}
              className={`category-btn ${selectedCategory === cat ? 'active' : ''}`}
              onClick={() => setSelectedCategory(cat)}
            >
              {cat}
            </button>
          ))}
        </div>

        <button className="add-btn" onClick={() => {
          setEditingRole(null);
          setNewRole({ title: '', category: 'Image', prompt: '', favorite: false });
          setShowAddModal(true);
        }}>
          + 새 템플릿 추가
        </button>
      </div>

      <div className="roles-grid">
        {filteredRoles.map(role => (
          <div key={role.id} className="role-card">
            <div className="role-header">
              <h3>{role.title}</h3>
              <div className="role-actions">
                <button
                  className={`fav-btn ${role.favorite ? 'favorited' : ''}`}
                  onClick={() => toggleFavorite(role.id)}
                >
                  {role.favorite ? '★' : '☆'}
                </button>
                <button className="edit-btn" onClick={() => handleEditRole(role)}>
                  ✏️
                </button>
                <button className="delete-btn" onClick={() => handleDeleteRole(role.id)}>
                  🗑️
                </button>
              </div>
            </div>
            <span className="role-category">{role.category}</span>
            <p className="role-prompt">{role.prompt}</p>
            <button className="copy-btn" onClick={() => copyPrompt(role.prompt)}>
              📋 복사하기
            </button>
          </div>
        ))}
      </div>

      {filteredRoles.length === 0 && (
        <div className="empty-state">
          <p>검색 결과가 없습니다.</p>
        </div>
      )}

      {showAddModal && (
        <div className="modal-overlay" onClick={() => setShowAddModal(false)}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <h2>{editingRole ? '템플릿 수정' : '새 템플릿 추가'}</h2>

            <input
              type="text"
              placeholder="제목"
              className="modal-input"
              value={newRole.title}
              onChange={(e) => setNewRole({ ...newRole, title: e.target.value })}
            />

            <select
              className="modal-select"
              value={newRole.category}
              onChange={(e) => setNewRole({ ...newRole, category: e.target.value })}
            >
              <option value="Image">Image</option>
              <option value="Video">Video</option>
              <option value="Animation">Animation</option>
            </select>

            <textarea
              placeholder="프롬프트 내용"
              className="modal-textarea"
              value={newRole.prompt}
              onChange={(e) => setNewRole({ ...newRole, prompt: e.target.value })}
              rows={6}
            />

            <div className="modal-actions">
              <button className="cancel-btn" onClick={() => {
                setShowAddModal(false);
                setEditingRole(null);
                setNewRole({ title: '', category: 'Image', prompt: '', favorite: false });
              }}>
                취소
              </button>
              <button
                className="save-btn"
                onClick={editingRole ? handleUpdateRole : handleAddRole}
              >
                {editingRole ? '수정' : '추가'}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;

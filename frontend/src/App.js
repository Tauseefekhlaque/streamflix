import { useEffect, useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

const API = 'http://127.0.0.1:8000/api';

export default function App() {
  const [movies, setMovies] = useState([]);
  const [search, setSearch] = useState('');
  const [token, setToken] = useState(localStorage.getItem('token'));

  useEffect(() => {
    axios.get(`${API}/movies/?search=${search}`).then(res => setMovies(res.data));
  }, [search]);

  const login = async () => {
    // Note: We are using 'tekhl' as username. You will need to enter your superuser password in the browser prompt.
    const password = prompt("Enter your superuser password (e.g., Admin@12345):");
    if (!password) return;
    
    try {
      const res = await axios.post(`${API}/login/`, {
        username: 'tekhl', 
        password: password
      });
      localStorage.setItem('token', res.data.access);
      setToken(res.data.access);
      alert('Logged in successfully! ❤️');
    } catch (err) {
      alert('Login failed. Check your password.');
    }
  };

  const addToList = async (movieId) => {
    if (!token) return alert('Please Login first (top right button)');
    try {
      await axios.post(`${API}/mylist/`, { movie_id: movieId }, {
        headers: { Authorization: `Bearer ${token}` }
      });
      alert('Added to My List ❤️');
    } catch (err) {
      alert('Already in your list!');
    }
  };

  return (
    <div className="min-vh-100" style={{ background: '#141414', color: 'white' }}>
      {/* Navbar */}
      <nav className="d-flex justify-content-between align-items-center p-3"
           style={{ background: 'black', borderBottom: '1px solid #333', position: 'sticky', top: 0, zIndex: 100 }}>
        <h3 style={{ color: '#E50914', fontWeight: 'bold', margin: 0, letterSpacing: '1px' }}>
          STREAMFLIX
        </h3>
        <div className="d-flex gap-2">
          <input 
            className="form-control" 
            placeholder="Search movies..."
            style={{ width: 250, background: '#222', color: 'white', border: '1px solid #444' }}
            onChange={e => setSearch(e.target.value)} 
          />
          {!token && (
            <button className="btn btn-danger fw-bold" onClick={login}>
              Login
            </button>
          )}
        </div>
      </nav>

      {/* Movie Grid */}
      <div className="container-fluid p-4">
        <h4 className="mb-4 text-light">Popular on StreamFlix</h4>
        <div className="row g-4">
          {movies.map(m => (
            <div key={m.id} className="col-6 col-md-4 col-lg-3">
              <div className="card border-0 h-100" style={{ background: '#1c1c1c', borderRadius: '8px', overflow: 'hidden' }}>
                <img 
                  src={m.poster} 
                  className="card-img-top" 
                  alt={m.title}
                  style={{ height: 350, objectFit: 'cover' }} 
                />
                <div className="card-body p-3 d-flex flex-column">
                  <h6 className="text-white mb-1 fw-bold">{m.title}</h6>
                  <small className="text-muted mb-3">{m.year} • ⭐ {m.rating}</small>
                  <button 
                    className="btn btn-sm btn-outline-danger mt-auto w-100 fw-bold"
                    onClick={() => addToList(m.id)}
                  >
                    + My List
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
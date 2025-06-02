import { useState } from 'react';
import Title from './components/Title';
import SearchBar from './components/SearchBar';
import MethodButtons from './components/MethodButtons';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState(null);

  const handleSearchTFIDF = async () => {
    try {
      const response = await fetch(`http://localhost:8000/api/search/tfidf?query=${encodeURIComponent(query)}`);
      const data = await response.json();
      setResults(data.results);
    } catch (error) {
      console.error('Error al buscar con TF-IDF:', error);
    }
  };

  const handleSearchBM25 = async () => {
    try {
      const response = await fetch(`http://localhost:8000/api/search/bm25?query=${encodeURIComponent(query)}`);
      const data = await response.json();
      setResults(data.results);
    } catch (error) {
      console.error('Error al buscar con BM25:', error);
    }
  };

  return (
    <div style={{ textAlign: 'center', padding: '2rem' }}>
      <Title />
      <SearchBar query={query} setQuery={setQuery} />
      <MethodButtons
        onSearchTFIDF={handleSearchTFIDF}
        onSearchBM25={handleSearchBM25}
      />
      {results && (
        <div style={{ marginTop: '2rem', textAlign: 'left', padding: '1rem' }}>
          <h3>Resultados:</h3>
          <ul>
            {results.map((res, idx) => (
              <li key={idx} style={{ marginBottom: '1rem' }}>{res}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;

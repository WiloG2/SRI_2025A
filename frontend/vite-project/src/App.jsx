import { useState } from 'react';
import Title from './components/Title';
import SearchBar from './components/SearchBar';
import MethodButtons from './components/MethodButtons';

function App() {
  const [query, setQuery] = useState('');

  const handleSearchTFIDF = () => {
    // Aquí puedes hacer una petición a tu backend en Java
    console.log('Buscando con TF-IDF:', query);
  };

  const handleSearchBM25 = () => {
    // Aquí puedes hacer una petición a tu backend en Java
    console.log('Buscando con BM25:', query);
  };

  return (
    <div style={{ textAlign: 'center', padding: '2rem' }}>
      <Title />
      <SearchBar query={query} setQuery={setQuery} />
      <MethodButtons
        onSearchTFIDF={handleSearchTFIDF}
        onSearchBM25={handleSearchBM25}
      />
    </div>
  );
}

export default App;

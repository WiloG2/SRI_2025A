const MethodButtons = ({ onSearchTFIDF, onSearchBM25 }) => {
  return (
    <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
      <button onClick={onSearchTFIDF}>TF-IDF</button>
      <button onClick={onSearchBM25}>BM25</button>
    </div>
  );
};

export default MethodButtons;

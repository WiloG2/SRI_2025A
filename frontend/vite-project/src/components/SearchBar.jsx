const SearchBar = ({ query, setQuery }) => {
  return (
    <input
      type="text"
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      placeholder="Escribe tu búsqueda..."
      style={{
        padding: '0.5rem',
        width: '60%',
        fontSize: '1rem',
        marginBottom: '1rem'
      }}
    />
  );
};

export default SearchBar;

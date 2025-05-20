import React, { useState } from 'react';
import axios from 'axios';
import SearchResults from './SearchResults';
import Profile from './Profile';

const SearchInput = () => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [error, setError] = useState(null);

    const handleSearch = async () => {
        const response = await axios.get(`https://django-react-website.onrender.com/api/books/?q=${query}`,
        {
            headers: {
                'Authorization': `Api-Key ${import.meta.env.VITE_API_KEY}`,
       },
    })
    .then(response => {
        setResults(response.data);
})
.catch(error => {
  setError(error.message);
});
  };

    return (
        <div>

            <div className="searchInput">
            <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} />
            <button onClick={handleSearch}>Search</button>
            </div>
            <div className="result">
            <SearchResults results={results} />
            </div>

            <div className="result">
            <Profile token={token} profile={profile} error={error}/>
            </div>
        </div>
    );
};

export default SearchInput;

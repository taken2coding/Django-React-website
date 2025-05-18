import React, { useState } from 'react';
import axios from 'axios';
import SearchResults from './SearchResults';

const SearchInput = () => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);

    const handleSearch = async () => {
        const response = await axios.get(`https://django-react-website.onrender.com/api/books/?q=${query}`);
        setResults(response.data);
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
        </div>
    );
};

export default SearchInput;

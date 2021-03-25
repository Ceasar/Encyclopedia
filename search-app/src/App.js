import React, { Component, useCallback, useEffect, useState } from 'react';
import algoliasearch from 'algoliasearch/lite';
import {
  InstantSearch,
  Hits,
  SearchBox,
  Pagination,
  connectSearchBox,
} from 'react-instantsearch-dom';
import PropTypes from 'prop-types';
import './App.css';

const searchClient = algoliasearch(
  '28JIW5EDOG',
  '910b4fc3f464a9b710bbfffccf00d027'
);

const simpleLinkPattern = /.*?\s([\w-]+)_.*?/gm;

const parseLinks = function(text) {
  return Array.from(text.matchAll(simpleLinkPattern), m => m[1])
}

function CardTextArea({currentRefinement, isSearchStalled, refine}) {
  const [links, setLinks] = useState([]);
  const onChange = useCallback((event) => {
    setLinks(parseLinks(event.target.value));
  }, [setLinks]);
  useEffect(() => {
    refine(links);
  }, [links]);
  return (
    <div>
      <p>{links}</p>
      <textarea onChange={onChange} />
    </div>
  );
}

const CardInput = connectSearchBox(CardTextArea);

class App extends Component {
  render() {
    return (
      <div>
        <header className="header">
          <h1 className="header-title">
            <a href="/">search-app</a>
          </h1>
        </header>

        <div className="container">
          <InstantSearch searchClient={searchClient} indexName="cards">
            <div className="search-panel">
              <CardInput />
              <div className="search-panel__results">
                <Hits hitComponent={Hit} />

                <div className="pagination">
                  <Pagination />
                </div>
              </div>
            </div>
          </InstantSearch>
        </div>
      </div>
    );
  }
}

function Hit({hit}) {
  return (
    <article>
      <p>{hit.text}</p>
      <p className="source">{hit.document}</p>
    </article>
  );
}

Hit.propTypes = {
  hit: PropTypes.object.isRequired,
};

export default App;

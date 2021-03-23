// Replace with your own values
const searchClient = algoliasearch(
  '28JIW5EDOG',
  '910b4fc3f464a9b710bbfffccf00d027' // search only API key, not admin API key
);

const search = instantsearch({
  indexName: 'cards',
  searchClient,
  routing: true,
});

search.addWidgets([
  instantsearch.widgets.configure({
    hitsPerPage: 32,
  })
]);

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#search-box',
    placeholder: 'Search for cards',
  })
]);

search.addWidgets([
  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
      item: document.getElementById('hit-template').innerHTML,
      empty: `We didn't find any results for the search <em>"{{query}}"</em>`,
    },
  })
]);

search.start();

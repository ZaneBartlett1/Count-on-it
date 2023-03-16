<script lang="ts">
  import { onMount } from 'svelte';
  import { createEventDispatcher } from 'svelte';

  export let counters = [];
  let isCounterOpen = false;

  const dispatch = createEventDispatcher();

  let toggleCounter = () => {
    isCounterOpen = !isCounterOpen;
  }

  let addCounter = () => {
    const newCounterName = prompt('Enter the name of the new counter:');
    if (newCounterName) {
      fetch(`http://127.0.0.1:5000/add-counter/${newCounterName}`, {method: 'POST'});
      // Dispatch an event to notify the main component that a new counter was added
      dispatch('addCounter', { name: newCounterName});
      }
  }

  let showDeleteOptions = (event) => {
    const name = event.target.dataset.name;
    const deleteOption = prompt('Delete counter? Hit Enter or OK to delete', '');
    if (deleteOption === '') {
      fetch(`http://127.0.0.1:5000/delete-counter/${name}`, {method: 'DELETE'});
      // Dispatch an event to notify the main component that a counter was deleted
      dispatch('deleteCounter', { name: name });
    }
  }


  const deleteCounter = (name) => {
    counters = counters.filter(counter => counter.name !== name);
  }

  onMount(() => {
    fetch('http://127.0.0.1:5000/get-counters')
      .then(response => response.json())
      .then(data => counters = data);
  });
</script>


<aside class="sidebar">
  <h2>Views</h2>
  <h2>
    <span class="arrow-icon" on:click={toggleCounter}>{isCounterOpen ? '▾' : '▸'}</span>
    <span>Counters</span>
    <button class="add-counter-button" on:click={addCounter}>+</button>
  </h2>
  {#if isCounterOpen}
    <ul class="counter-list">
      {#each counters as counter}
      <li>
        <span>{counter.name}</span>
        <button class="delete-counter-button" on:click={showDeleteOptions} data-name={counter.name}></button>
      </li>
    {/each}
    
    </ul>
  {/if}
  <h2>Logs</h2>
</aside>


<style>
  .sidebar {
    background-color: #1a1a1a;
    padding: 20px;
    width: 200px;
    position: fixed;
    left: 0;
    top: 0;
    bottom: 0;
  }

  .arrow-icon {
    cursor: pointer;
    padding: 3px 5px;
    border-radius: 3px;
  }

  .arrow-icon:hover {
    background-color: #333;
  }

  .add-counter-button {
    color: white;
    border: none;
    padding: 3px 5px;
    border-radius: 3px;
    cursor: pointer;
    margin-left: 10px;
    font-size: 1em;
    line-height: 1.5;
  }

  .add-counter-button:hover {
    background-color: #333;
  }

  .counter-list {
    list-style: none;
    margin: 0;
    padding: 0;
  }

  .counter-list li {
    padding: 5px;
  }

  .counter-list li:hover,
  .counter-list li:hover .delete-counter-button {
    background-color: #333;
  }

  .counter-list li:hover .delete-counter-button::after {
    content: "...";
    display: inline-block;
    vertical-align: middle;
    margin-left: 5px;
    opacity: 1;
  }

  .delete-counter-button {
    color: white;
    border: none;
    padding: 6px 10px;
    border-radius: 3px;
    cursor: pointer;
    margin-left: 10px;
    font-size: 1.5em;
    line-height: 0; 
  }

  .delete-counter-button:hover {
    background-color: #333;
  }

  .delete-counter-button::after {
    content: "";
    display: inline-block;
    border-radius: 50%;
    opacity: 0;
    transition: opacity 0.2s ease-in-out;
  }

  .delete-counter-button:hover::after {
    opacity: 1;
  }

</style>

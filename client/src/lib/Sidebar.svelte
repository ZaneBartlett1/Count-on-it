<script lang="ts">
  import { onMount } from 'svelte';
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  export let counters = [];
  let isCounterOpen = false;

  function toggleCounter() {
    isCounterOpen = !isCounterOpen;
  }

  function addCounter() {
    const newCounterName = prompt('Enter the name of the new counter:');
    if (newCounterName) {
      fetch(`http://127.0.0.1:5000/add-counter/${newCounterName}`, {method: 'POST'});
      // Dispatch an event to notify the main component that a new counter was added
      dispatch('addCounter', { name: newCounterName });
  }
}
</script>

<aside class="sidebar">
  <h2>Views</h2>
  <h2 on:click={toggleCounter}>
    <i class="arrow-icon">{isCounterOpen ? '▾' : '▸'}</i>
    Counters
    <button class="add-counter-button" on:click={addCounter}>+</button>
  </h2>
  {#if isCounterOpen}
    <ul class="counter-list">
      {#each counters as counter}
        <li>{counter.name}</li>
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
    margin-right: 5px;
  }

  h2 {
    cursor: pointer;
  }

  h2:hover {
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

  .add-counter-button {
    background-color: #333;
    color: white;
    border: none;
    padding: 3px 5px;
    border-radius: 3px;
    cursor: pointer;
    margin-left: 10px;
  }
</style>

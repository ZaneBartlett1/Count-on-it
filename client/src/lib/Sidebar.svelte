<script lang="ts">
  import { onMount } from 'svelte';
  import { createEventDispatcher } from 'svelte';

  export let counters = [];

  
  let isCounterOpen = false;
  let selectedCounter = {name: null};

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

  let showOptions = (event) => {
    const clickedCounterName = event.target.dataset.name;
    if (selectedCounter === clickedCounterName) {
      selectedCounter = null;
    } else {
      selectedCounter = clickedCounterName;
    }
  }

  let deleteCounter = () => {
    fetch(`http://127.0.0.1:5000/delete-counter/${selectedCounter}`, {method: 'DELETE'});
    // Dispatch an event to notify the main component that a counter was deleted
    dispatch('deleteCounter', { name: selectedCounter });
    counters = counters.filter(counter => counter.name !== selectedCounter);
    selectedCounter = null; // reset the selected counter
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
          <button class="general-button" on:click={showOptions} data-name={counter.name}>...</button>
          {#if selectedCounter === counter.name}
            <div class="modal">
              <button class="general-button" on:click={deleteCounter}>Delete</button>
            </div>
          {/if}
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
    border: none;
    padding: 3px 5px;
    border-radius: 3px;
    margin-left: 10px;
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

  .counter-list li:hover {
    background-color: #333;
  }

  .general-button {
    padding: 10px;
    margin: 3px;
    margin-left: 10px;
    line-height: 0;
  }


</style>

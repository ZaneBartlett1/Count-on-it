<script lang="ts">
  import { onMount } from 'svelte';

  export let counters = [];
  let isCounterOpen = false;
  

  onMount(() => {
    fetch('http://localhost:5000/counters')
      .then(res => res.json())
      .then(data => {
        counters = data.map(counter => counter.Name);
      });
  });

  function toggleCounter() {
    isCounterOpen = !isCounterOpen;
  }

</script>

<aside class="sidebar">
  <h2>Views</h2>
  <h2 on:click={toggleCounter}>
    <i class="arrow-icon">{isCounterOpen ? '▾' : '▸'}</i>
    Counters
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
</style>

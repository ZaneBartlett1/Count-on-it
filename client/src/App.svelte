<script lang="ts">
  import { onMount } from 'svelte';
  import Counter from './lib/Counter.svelte';
  import AddCounter from './lib/AddCounter.svelte';
  import Sidebar from './lib/Sidebar.svelte';

  let counters = [];

  function addCounter(newCounter) {
    const counter = { name: newCounter.detail.detail.name, count: 0 };
    counters = [...counters, counter];
  }

  onMount(() => {
    fetch('http://localhost:5000/counters')
      .then(res => res.json())
      .then(data => {
        counters = data.map(counter => ({
          name: counter.Name,
          count: counter.Count
        }));
      });
  });
</script>

<main>
  <Sidebar {counters} />
  <AddCounter on:addCounter={addCounter} />
  <div>
    {#each counters as counter}
    <Counter name={counter.name} count={counter.count} />
    {/each}
  </div>
</main>

<style>
  main {
    display: grid;
    grid-template-columns: 1fr 5fr;
  }
</style>

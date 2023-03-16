<script lang="ts">
  import { onMount } from 'svelte';
  import Counter from './lib/Counter.svelte';
  import Sidebar from './lib/Sidebar.svelte';

  let counters = [];

  let addCounter = (newCounter) => {
    const counter = {name: newCounter.detail.name};
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
  <Sidebar {counters} on:addCounter={addCounter}/>
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

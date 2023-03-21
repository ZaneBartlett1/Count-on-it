<script lang="ts">
  import { onMount } from 'svelte';
  import Sidebar from './lib/Sidebar.svelte';
  import Spreadsheet from './lib/Spreadsheet.svelte';

  let counters = [];

  let addCounter = (event) => {
    const newCounter = {
      id: event.detail.detail.id,
      name: event.detail.detail.name,
      count: event.detail.detail.count
    };
    counters = [...counters, newCounter];
  };

  onMount(() => {
    fetch('http://localhost:5000/counters')
      .then(res => res.json())
      .then(data => {
        counters = data.map(counter => ({
          id: counter.id,
          name: counter.Name,
          count: counter.Count
        }));
      });
  });
</script>

<main>
  <Sidebar {counters} on:addCounter={addCounter} />
  <div>
    <Spreadsheet {counters} />
  </div>
</main>

<style>
  main {
    display: grid;
    grid-template-columns: 1fr 5fr;
  }
</style>

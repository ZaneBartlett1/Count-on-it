<script lang="ts">
  import { onMount } from "svelte";
  import Sidebar from "./lib/Sidebar.svelte";
  import Spreadsheet from "./lib/Spreadsheet.svelte";

  interface Counter {
    id: number;
    name: string;
    count: number;
  }

  let counters: Counter[] = [];

  /**
   * Adds a new counter to the counters array.
   * @param {CustomEvent} event - The custom event containing the new counter's details.
   */
  let addCounter = (event: CustomEvent) => {
    const newCounter: Counter = {
      id: event.detail.detail.id,
      name: event.detail.detail.name,
      count: event.detail.detail.count,
    };
    counters = [...counters, newCounter];
  };

  /**
   * Deletes selected counter
   * @param {CustomEvent} event - The custom event containing the new counter's details.
   */
  let deleteCounter = (event: CustomEvent) => {
    counters = counters.filter((counter) => counter.name !== event.detail.name);
  };

  onMount(() => {
    fetch("http://localhost:5000/counters")
      .then((res) => res.json())
      .then((data) => {
        counters = data.map((counter: any) => ({
          id: counter.id,
          name: counter.Name,
          count: counter.Count,
        }));
      });
  });
</script>

<main>
  <Sidebar
    {counters}
    on:addCounter={addCounter}
    on:deleteCounter={deleteCounter}
  />
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

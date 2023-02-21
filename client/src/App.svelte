<script lang="ts">
  import Counter from './lib/Counter.svelte';
  import AddCounter from './lib/AddCounter.svelte';
  import Sidebar from './lib/Sidebar.svelte';

  let counters = [];

  function addCounter(newCounter) {
    const counter = { name: newCounter.detail.detail.name, count: 0 };
    counters = [...counters, counter];
  }


  let rand = -1;
  function getRand() {
    fetch("http://localhost:5000/rand")
      .then(d => d.text())
      .then(d => (rand = Number(d)))
  }
</script>

<main>
  <Sidebar />
  <div class="screen-container">
    <p>
      Your number is {rand}!
      <button on:click={getRand}>Get a random number</button>
    </p>
  </div>
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

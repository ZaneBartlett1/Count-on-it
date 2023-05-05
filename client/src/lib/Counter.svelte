<script lang="ts">
  export let count: number = 0;
  export let name: string = "";

  /**
   * Increments the count of the counter.
   */
  const increment = () => {
    fetch(`http://127.0.0.1:5000/increment/${name}`)
      .then((res) => res.json())
      .then((data) => {
        // Update count with response data
        count = data.count;
      })
      .catch((error) => {
        console.error(error);
      });
  };
</script>

<button on:click={increment}>
  {name}: <span id="counter">{count}</span>
</button>

<script lang="ts">
  export let count: number = 0;
  export let name: string = '';

  const increment = () => {
    count += 1;
  };
</script>

<button on:click={increment}>
  {name}: {count}
</button>

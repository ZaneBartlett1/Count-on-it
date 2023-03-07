<script>
  import { createEventDispatcher } from 'svelte';
  import Counter from './Counter.svelte';

  let name = '';

  const dispatch = createEventDispatcher();

  function handleSubmit(event) {
    event.preventDefault();
    const newCounter = { name, count: 0 };
    // Dispatch an event to notify the main component that a new counter was added
    dispatch('addCounter', { detail: newCounter });
    // Reset the name
    name = '';
  }

</script>

<form on:submit={handleSubmit}>
  <input type="text" bind:value={name} placeholder="Enter a name for the new counter" />
  <button type="submit">Add counter</button>
</form>

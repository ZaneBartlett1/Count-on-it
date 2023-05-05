<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import Counter from "./Counter.svelte";

  let name = "";

  const dispatch = createEventDispatcher();

  /**
   * Handles the form submission, adding a new counter.
   * @param {Event} event - The submit event.
   */
  function handleSubmit(event: Event) {
    event.preventDefault();
    const newCounter = { name, count: 0 };
    fetch(`http://127.0.0.1:5000/add-counter/${name}`, { method: "POST" });
    // Dispatch an event to notify the main component that a new counter was added
    dispatch("addCounter", { detail: newCounter });
    // Reset the name
    name = "";
  }
</script>

<form on:submit={handleSubmit}>
  <input
    type="text"
    bind:value={name}
    placeholder="Enter a name for the new counter"
  />
  <button type="submit">Add counter</button>
</form>

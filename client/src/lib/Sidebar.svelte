<script lang="ts">
  import { createEventDispatcher } from "svelte";

  export let counters = [];

  interface Counter {
    id: number;
    name: string;
    count: number;
  }

  let isCounterOpen = false;
  let selectedCounter: string | null = null;

  const dispatch = createEventDispatcher();

  /**
   * Toggles the visibility of the counter list.
   */
  let toggleCounter = () => {
    isCounterOpen = !isCounterOpen;
  };

  /**
   * Adds a new counter and dispatches an event to notify the parent component.
   */
  let addCounter = async () => {
    const newCounterName = prompt("Enter the name of the new counter:");
    if (newCounterName) {
      const response = await fetch(
        `http://127.0.0.1:5000/add-counter/${newCounterName}`,
        { method: "POST" }
      );
      const data = await response.json();
      if (!data.error) {
        const newCounter: Counter = {
          id: data.id,
          name: newCounterName,
          count: 0,
        };
        dispatch("addCounter", { detail: newCounter });
      } else {
        alert(data.error);
      }
    }
  };

  /**
   * Toggles the visibility of the options for a counter.
   * @param {Event} event - The click event.
   */
  let showOptions = (event: Event) => {
    const clickedCounterName = (event.target as HTMLElement).dataset.name;
    if (selectedCounter === clickedCounterName) {
      selectedCounter = null;
    } else {
      selectedCounter = clickedCounterName;
    }
  };

  /**
   * Deletes the selected counter and dispatches an event to notify the parent component.
   */
  let deleteCounter = () => {
    fetch(`http://127.0.0.1:5000/delete-counter/${selectedCounter}`, {
      method: "DELETE",
    });
    // Dispatch an event to notify the main component that a counter was deleted
    dispatch("deleteCounter", { name: selectedCounter });
    counters = counters.filter(
      (counter: Counter) => counter.name !== selectedCounter
    );
    selectedCounter = null; // reset the selected counter
  };
</script>

<aside class="sidebar">
  <h2>Views</h2>
  <h2>
    <span class="arrow-icon" on:click={toggleCounter}
      >{isCounterOpen ? "▾" : "▸"}</span
    >
    <span>Counters</span>
    <button class="add-counter-button" on:click={addCounter}>+</button>
  </h2>
  {#if isCounterOpen}
    <ul class="counter-list">
      {#each counters as counter}
        <li>
          <span>{counter.name}</span>
          <button
            class="general-button"
            on:click={showOptions}
            data-name={counter.name}>...</button
          >
          {#if selectedCounter === counter.name}
            <div class="modal">
              <button class="general-button" on:click={deleteCounter}
                >Delete</button
              >
            </div>
          {/if}
        </li>
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
    cursor: pointer;
    padding: 3px 5px;
    border-radius: 3px;
  }

  .arrow-icon:hover {
    background-color: #333;
  }

  .add-counter-button {
    border: none;
    padding: 3px 5px;
    border-radius: 3px;
    margin-left: 10px;
    line-height: 1.5;
  }

  .add-counter-button:hover {
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

  .counter-list li:hover {
    background-color: #333;
  }

  .general-button {
    padding: 10px;
    margin: 3px;
    margin-left: 10px;
    line-height: 0;
  }
</style>

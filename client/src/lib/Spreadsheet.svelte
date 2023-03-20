<script>
    import { onMount } from 'svelte';
  
    let headers = [];
    let rows = [];
    
  
    onMount(async () => {
      const res = await fetch('http://localhost:5000/counters');
      const data = await res.json();
      headers = Object.keys(data[0]);
      rows = data.map(row => Object.values(row));
      addEmptyRowsAndColumns();
    });
  
    const updateTable = async () => {
      const res = await fetch('http://localhost:5000/counters');
      const data = await res.json();
      headers = Object.keys(data[0]);
      rows = data.map(row => Object.values(row));
      addEmptyRowsAndColumns();
    };
  
    const addEmptyRowsAndColumns = () => {
      const totalColumns = 15;
      const totalRows = 30;
  
      while (headers.length < totalColumns) {
        headers.push('');
      }
  
      rows = rows.map(row => {
        while (row.length < totalColumns) {
          row.push('');
        }
        return row;
      });
  
      while (rows.length < totalRows) {
        const emptyRow = new Array(totalColumns).fill('');
        rows.push(emptyRow);
      }
    };
  </script>
  
  <table>
    <thead>
      <tr>
        {#each headers as header}
          <th>{header}</th>
        {/each}
      </tr>
    </thead>
    <tbody>
      {#each rows as row}
        <tr>
          {#each row as cell}
            <td>{cell}</td>
          {/each}
        </tr>
      {/each}
    </tbody>
  </table>
  
  <style>
    table {
      width: 100%;
      border-collapse: collapse;
      background-color: #f2f2f2;
      color: black;
      font-family: Arial, sans-serif;
      margin-left: -80px; /* Remove the margin between the sidebar and the main view */
    }
    th,
    td {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: left;
      min-width: 95px;
    }
  </style>
  
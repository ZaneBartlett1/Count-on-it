# Count-on-it

* Primary goal is to practice being able to use Vite and Svelte for front end and do back end unit testing (just for python really) at a not complete shit level. May also be good to try to practice api requests for outside the app, but not a primary goal.

* For the app itself - Ideally I'd want something that would be powerful enough to basically track progress for a movie/show/book etc, producing a list and also be flexiable enough that it could also be used to nicely track simple events like how many times someone finishes their cup of water, goes for a walk, etc

* I think tracking events is what I'll start with as a MVP and possibly look at doing the more ideal/powerful stuff from there if I'm still going strong

  
### Figure out how to map counters to table(s)
  * Also, unless it's on one big table I'd like to have the functionality as Asana where you can create unique columns on a table (project in Asana) or pick from a library, with that library just being other columns you've said should be selectable across tables. Editing any column in a library edits the column across tables
  * If each counter has it's own table this might cause issues because you can only join up to 64 tables at once. Something feels wrong about this method.
  * The "most optimal" seems to be something where you'd have a table and match counters to that, making a new table if enough of the columns didn't overlap, but that seems clunky.
    * Also what happens if you have a table for shows and movies, and another for books, but then you want to look at all your stories. You've named the column for the name in shows and movies "show/movie name", and in books "book name", but want it to say "name" when looking at both tables. I think there isn't going to be a great way to deal with this that doesn't add undue complexity. I think the best route is really trying to add the functionality of being able to add columns to a library and select from that library across tables. Editing a column in one table edits it across tables. so that they're kept in sync across tables. That way if someone wants them to be lined up when they select multiple coutners from different tables, the name will for sure match. Even in this case it's a bit frustrating though just because I could imagine the want to have "episodes" for a show and "chapters" for a book, but want the columns to line up and say "episodes/chapters" if you had both counters selected. In this data model, you'd either have to have them be different columns (which I'm sure some people would actually prefer) or have the abstract version of episodes and chapters, something like "sections".
  * Something that is a good arguement for having it all on one big table is that it helps alivate the entire issue making column names match so that the tables are clean if you want to view counters from multiple tables sense they're all on the same table. This would also make it easier to have it so that under a certain view, a single column is named something else.

### Header
  * Drop down to say if you want to look at the counters, logs, or both
  * Filters, let's you do basic filters on a row based on a column like "less than x"
  * Columns, let's you select which columns to view
  * Export, exports to csv
  * Sort, as basic as filtering
  * SQL, for the advanced

### Main screen section that shows the currently toggled visible counters either -
  * As the counters themselves
  * A spreadsheet style log of counter clicks
  * Both

### Side bar
  * "Views" which is just saved views
      * Would mostly just save if you're looking at log or counter view and any relevant header info like filters, columns, sort.
      * Might be worth considering have nested views. So that someone could have "stories" and then "books", "TV", "Movies" under that.
  * Possibly have a "Tables" section, this would only be if I went with the idea that there would be different tables that you attach counters to
  * User created sections (So I imagine this is like how in Asana a project needs to be in a team, but can be in multiple porfolios, which here is views)
      * Maybe one premade section called "counters" or something just to start. Editable and deletable.
      * Used to group counters
      * Clicking the counter should pull up a view that's just the counter and the logs of clicks from that counter. Like how clicking it in Asana brings you to a default saved view of the project
      * Able to toogle the entire section on or off
      
      
Example 
![PXL_20230112_033520178](https://user-images.githubusercontent.com/85081861/211969887-edb5ce13-9ef9-4cfa-9b76-d8bd4656699e.jpg)

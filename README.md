# Button-Board

* Primary goal is to practice being able to use Vite and Svelte for front end and do back end unit testing (just for python really) at a not complete shit level. May also be good to try to practice api requests in this, but not a primary goal.

* For the app itself - Ideally I'd want something that would be powerful enough to basically track progress for a movie/show/book etc, producing a list and also be flexiable enough that it could also be used to nicely track simple events like how many times someone finishes their cup of water, goes for a walk, etc

* I think tracking events is what I'll start with as a MVP and possibly look at doing the more ideal/powerful stuff from there if I'm still going strong

* Something from Myanimelist is that you can add an anime and rate the entire thing, but also add each episode and rate the episode by itself, and there's no conflict. However their solution is to just not show you the average sum of rating from each episode at all. I'm not sure I prefer this, but I understand how in a lot of cases people would prefer to just be able to rate the overall show without *having* to go through each episode to get an overall rating. 
  * This could be solved by having something a column to identify parent rows and another for ratings, then for rating the series overall, there can be a calculated sum and what the viewer determined to be the best. This would imply that you could do calculated fields in the text box, which seems fairly complex, maybe there's a reason MAL didn't do this...
  
  
  
  After some thinking -
  
  * On the back-end every button could have it's own table, allowing for however many columns for each button
    * This might cause issues where you can only join up to 64 tables at once. Something feels wrong about this method. The "most optimal" seems to be something where you'd have a table and match buttons to that, but that seems clunky. Something that might be possible is just checking after a new button is made, if there's a table that already has columns with those same names and data types. Something about that seems weird though too. This kind of goes back to, you could have everything on basically a two tables, buttons, and their outputs.
    * I'd like to handle this like Asana where you can create unique columns or pick from a library, with that library just being other columns you've said should be selectable across tables. 
    * There would be a table that is just the concatination of everything by event time. This would be the "log"
      * I'm tempted to, on the table for each button, have a created date, and include the buttons themselves on this log.
  * Main screen section that is either -
    * A list of all the buttons currently toogled visable with options - edit names, increment, delete, etc
      * Every button should be able to, on some specific click, do something that shows just the logs of clicks from that button. I like the idea of it staying on the main page and doing a dropdown of sorts, but taking you to the logs page with it filtered to just that button would also work.
      * Thinking about what columns would be exposed here is kinda hard. I guess the user could select which ones, with an edit by each always avaliable to edit settings for that button. Like if they want to have a wizard pop up and ask for more information or if it should be very basic and just update the log that the button was clicked at a certain time and increment the button.
    * A spreadsheet style log of button clicks with all other information
      * This should be filterable to what buttons you want to look at as well as columns. Whatever is being shown can be exported 
  * Side bar that you can create groups of buttons in. MAL is sort of kind of, if you squint, what I would want this to look like.
    * Add button
      * This would largely look like making a new table, defining column data types, etc.
    * Possibly have a "Tables" section, this would only be if I went with the idea that there would be different tables that you attach buttons to
    * Radio button to show either the buttons or log view
    * A special section "views" which is just saved views
      * Would mostly just save if you're looking at log or button view, what buttons you have toggled, and what columns you have toggled.
      * Might be worth considering have nested views. So that someone could have "stories" and then "books", "TV", "Movies" under that.
    * User created sections (This starts to feel like just a redundent and weaker version of views. It's nice to have, but I think if there's just a "buttons" section that you can toggle which buttons, select the columns, and then save that to a view, this is literally just a nice to have)
      * Maybe one premade section called "buttons" or something just to start. Editable and deletable.
      * Used to group buttons 
      * toggle what buttons are being shown/or logs from buttons, depending on view
      * Able to toogle the entire section on or off
      * Collpasable

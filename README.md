# Count-on-it

* Primary goal is to practice being able to use Vite and Svelte for front end and do back end unit testing (just for python really) at a not complete shit level. May also be good to try to practice api requests for outside the app, but not a primary goal.

* For the app itself - Ideally I'd want something that would be powerful enough to basically track progress for a movie/show/book etc, producing a list and also be flexiable enough that it could also be used to nicely track simple events like how many times someone finishes their cup of water, goes for a walk, etc

* I think tracking events is what I'll start with as a MVP and possibly look at doing the more ideal/powerful stuff from there if I'm still going strong

### Tables

#### Counter table

* Going to do it all on one big table. This helps alivate the entire issue making column names match between tables for counters so that the tables. Instead in the view I'll allow users to save the name as something other than what it's actually called, giving it an alias. So you'd have a generic name column for your books, movies, shows, etc, but then when you're viewing it under a view called something like "anime", the name will appear as "Anime name" or something instead. Nothing is saved if it's not saved to a view. 

#### Log table

* This will just be the output of the counters basically. It would have the same columns, and the views would work the same

#### Views table

* Most of this will just be the query that's generated and then saved by a question using a WYSIWYG editor. It will also have some properties like the ID, name, created date, etc. Would save if you're looking at log or counter view and any relevant header info like filters, columns, sort, and alias. Need to think of anything else to be included

#### Link table

* Used to link views to corrisponding counters, columns, filters, user's query, etc. I need to think about if I need multiple link tables for this, or just the one.
  
  ![image](https://user-images.githubusercontent.com/85081861/212760670-c2276661-d030-4af4-b8c8-3460e4b4e3a0.png)
  
  ```
  SELECT Counters.*
  FROM Counters
  JOIN CountersInView ON CountersInView.CounterID = Counters.ID
  JOIN Views ON Views.ID = CountersInView.ViewID
  WHERE Views.Name = 'anime' AND Counter.Score > 8;
  ```

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
* Both, I imagine something how it looks with a parent and subtask in Asana, but like instead of subtasks it's the logs
![image](https://user-images.githubusercontent.com/85081861/225187010-0aa0dfc1-dc90-4609-a3fb-28c6b721a67a.png)


### Side bar

* "Views" which is just saved views
  * Name that's mapped to a query, used by a view component to render counters/logs and apply filters
  * Might be worth considering have nested views. So that someone could have "stories" and then "books", "TV", "Movies" under that.
* Counters
  * This is just row on a spreadsheet looking view where each row is a counter
* Logs
  * This is basically like Counter, but for the longs. It'll be more than one row, but it'll still be filtered down to just the logs from that counter.

Example
![PXL_20230315_024839697~2](https://user-images.githubusercontent.com/85081861/225192802-cbf39aaa-ea69-4124-bc2e-6e0ab10dc14c.jpg)

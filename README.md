# Count-on-it

* As a project to improve my skills - Primary goal is to practice being able to use Vite and Svelte for front end and do unit testing (just for python really) at a basic level. May also be good to try to practice api requests for outside the app once I have things set up, but not a primary goal.

* For the app itself - Ideally I'd want something that would be powerful enough to basically track progress for a movie/show/book etc, producing a list and also be flexible enough that it could also be used to nicely track simple events like how many times someone finishes their cup of water, goes for a walk, etc. The way I would plan on doing this is having a table of event loggers, "counters", and when you "count" on them, you're really just doing one of two things - either logging an instance of that event, or you might literally be incrementing on the counter table. What I think is going to be very powerful about this is that the users would, ideally, be able to create columns on either the counter table or the log table. These columns would, ideally, be able to track values, but also do calculations. 

Example
![PXL_20230315_024839697~2](https://user-images.githubusercontent.com/85081861/225192802-cbf39aaa-ea69-4124-bc2e-6e0ab10dc14c.jpg)

Progress as of 2023/03/21

[Screencast from 03-21-2023 11:44:33 PM.webm](https://user-images.githubusercontent.com/85081861/226804620-c9f253bb-05ae-4cef-bba2-2a83dba79ee0.webm)

### Tables

#### Counter table

* Going to do it all on one big table. This helps alleviate the entire issue by making column names match between tables for counters so that the tables. Instead in the view I'll allow users to save the name as something other than what it's actually called, giving it an alias. So you'd have a generic name column for your books, movies, shows, etc, but then when you're viewing it under a view called something like "anime", the name will appear as "Anime name" or something instead. Nothing is saved if it's not saved to a view. 

#### Log table

* This will just be the output of the counters basically. It would have the same columns, and the views would work the same

#### Views table

* Most of this will just be the query that's generated and then saved by a question using a WYSIWYG editor. It will also have some properties like the ID, name, created date, etc. Would save if you're looking at log or counter view and any relevant header info like filters, columns, sort, and alias. Need to think of anything else to be included.

#### Link table

* Used to link views to corresponding counters, columns, filters, user's query, etc. I need to think about if I need multiple link tables for this, or just the one.
Basic example - 
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
  * This is basically like Counter, but for the logs. It'll be more than one row, but it'll still be filtered down to just the logs from that counter.

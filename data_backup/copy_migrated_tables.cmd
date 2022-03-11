REM Workbench Table Data copy script
REM Workbench Version: 8.0.27
REM 
REM Execute this to copy table data from a source RDBMS to MySQL.
REM Edit the options below to customize it. You will need to provide passwords, at least.
REM 
REM Source DB: Mysql@localhost:3306 (MySQL)
REM Target DB: Mysql@eanl4i1omny740jw.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306


@ECHO OFF
REM Source and target DB passwords
set arg_source_password=
set arg_target_password=
set arg_source_ssh_password=
set arg_target_ssh_password=


REM Set the location for wbcopytables.exe in this variable
set "wbcopytables_path=C:\Program Files\MySQL\MySQL Workbench 8.0"

if not [%wbcopytables_path%] == [] set wbcopytables_path=%wbcopytables_path%
set wbcopytables=%wbcopytables_path%\wbcopytables.exe

if not exist "%wbcopytables%" (
	echo "wbcopytables.exe doesn't exist in the supplied path. Please set 'wbcopytables_path' with the proper path(e.g. to Workbench binaries)"
	exit 1
)

IF [%arg_source_password%] == [] (
    IF [%arg_target_password%] == [] (
        IF [%arg_source_ssh_password%] == [] (
            IF [%arg_target_ssh_password%] == [] (
                ECHO WARNING: All source and target passwords are empty. You should edit this file to set them.
            )
        )
    )
)
set arg_worker_count=2
REM Uncomment the following options according to your needs

REM Whether target tables should be truncated before copy
REM set arg_truncate_target=--truncate-target
REM Enable debugging output
REM set arg_debug_output=--log-level=debug3


REM Creation of file with table definitions for copytable

set table_file=%TMP%\wb_tables_to_migrate.txt
TYPE NUL > %TMP%\wb_tables_to_migrate.txt
ECHO `s3p5x7kb9czupn46`	`categories`	`s3p5x7kb9czupn46`	`categories`	`id`	`id`	`id`, `name`, `created_at`, `updated_at` >> %TMP%\wb_tables_to_migrate.txt
ECHO `s3p5x7kb9czupn46`	`pages`	`s3p5x7kb9czupn46`	`pages`	`id`	`id`	`id`, `name`, `created_at`, `updated_at`, `user_id`, `is_public`, `custom_url`, `content`, `cover_picture`, `synopsis` >> %TMP%\wb_tables_to_migrate.txt
ECHO `s3p5x7kb9czupn46`	`people`	`s3p5x7kb9czupn46`	`people`	`id`	`id`	`id`, `first_name`, `last_name`, `created_at`, `updated_at`, `avatar`, `gender` >> %TMP%\wb_tables_to_migrate.txt
ECHO `s3p5x7kb9czupn46`	`playlists`	`s3p5x7kb9czupn46`	`playlists`	`id`	`id`	`id`, `month`, `year`, `created_at`, `updated_at`, `user_id`, `spotify_url` >> %TMP%\wb_tables_to_migrate.txt
ECHO `s3p5x7kb9czupn46`	`playlists_has_songs`	`s3p5x7kb9czupn46`	`playlists_has_songs`	`id`	`id`	`id`, `playlist_id`, `song_id`, `created_at`, `updated_at`, `playlists_has_songscol` >> %TMP%\wb_tables_to_migrate.txt
ECHO `s3p5x7kb9czupn46`	`post_has_people`	`s3p5x7kb9czupn46`	`post_has_people`	`people_id`,`post_id`	`people_id`,`post_id`	`people_id`, `post_id`, `created_at`, `updated_at` >> %TMP%\wb_tables_to_migrate.txt
ECHO `s3p5x7kb9czupn46`	`posts`	`s3p5x7kb9czupn46`	`posts`	`id`	`id`	`id`, `category_id`, `created_at`, `updated_at`, `is_featured`, `cover_picture`, `synopsis`, `user_id`, `content`, `name`, `is_public`, `posted_date` >> %TMP%\wb_tables_to_migrate.txt
ECHO `s3p5x7kb9czupn46`	`refit_pages`	`s3p5x7kb9czupn46`	`refit_pages`	`id`	`id`	`id`, `news`, `schedule`, `loc`, `about_me`, `user_id`, `created_at`, `updated_at`, `playlist_id`, `banner1_picture`, `banner2_picture`, `about_me_picture` >> %TMP%\wb_tables_to_migrate.txt
ECHO `s3p5x7kb9czupn46`	`songs`	`s3p5x7kb9czupn46`	`songs`	`id`	`id`	`id`, `name`, `artist`, `link`, `created_at`, `updated_at`, `user_id` >> %TMP%\wb_tables_to_migrate.txt
ECHO `s3p5x7kb9czupn46`	`users`	`s3p5x7kb9czupn46`	`users`	`id`	`id`	`id`, `first_name`, `last_name`, `email`, `pw`, `created_at`, `updated_at`, `is_verified` >> %TMP%\wb_tables_to_migrate.txt


"%wbcopytables%" ^
 --mysql-source="root@localhost:3306" ^
 --source-rdbms-type=Mysql ^
 --target="tsb8ie9awn4a20i3@eanl4i1omny740jw.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306" ^
 --source-password="%arg_source_password%" ^
 --target-password="%arg_target_password%" ^
 --table-file="%table_file%" ^
 --source-ssh-port="22" ^
 --source-ssh-host="" ^
 --source-ssh-user="" ^
 --target-ssh-port="22" ^
 --target-ssh-host="" ^
 --target-ssh-user="" ^
 --source-ssh-password="%arg_source_ssh_password%" ^
 --target-ssh-password="%arg_target_ssh_password%" --thread-count=%arg_worker_count% ^
 %arg_truncate_target% ^
 %arg_debug_output%

REM Removes the file with the table definitions
DEL %TMP%\wb_tables_to_migrate.txt



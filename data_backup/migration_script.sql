-- ----------------------------------------------------------------------------
-- MySQL Workbench Migration
-- Migrated Schemata: s3p5x7kb9czupn46
-- Source Schemata: s3p5x7kb9czupn46
-- Created: Thu Mar 10 18:47:48 2022
-- Workbench Version: 8.0.27
-- ----------------------------------------------------------------------------

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------------------------------------------------------
-- Schema s3p5x7kb9czupn46
-- ----------------------------------------------------------------------------
DROP SCHEMA IF EXISTS `s3p5x7kb9czupn46` ;
CREATE SCHEMA IF NOT EXISTS `s3p5x7kb9czupn46` ;

-- ----------------------------------------------------------------------------
-- Table s3p5x7kb9czupn46.categories
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `s3p5x7kb9czupn46`.`categories` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 19
DEFAULT CHARACTER SET = utf8mb3;

-- ----------------------------------------------------------------------------
-- Table s3p5x7kb9czupn46.pages
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `s3p5x7kb9czupn46`.`pages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `is_public` TINYINT NULL DEFAULT '0',
  `custom_url` VARCHAR(45) NULL DEFAULT NULL,
  `content` LONGTEXT NULL DEFAULT NULL,
  `cover_picture` VARCHAR(255) NULL DEFAULT NULL,
  `synopsis` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pages_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_pages_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `s3p5x7kb9czupn46`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = utf8mb3;

-- ----------------------------------------------------------------------------
-- Table s3p5x7kb9czupn46.people
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `s3p5x7kb9czupn46`.`people` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `avatar` VARCHAR(255) NULL DEFAULT NULL,
  `gender` VARCHAR(45) NOT NULL DEFAULT 'male',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb3;

-- ----------------------------------------------------------------------------
-- Table s3p5x7kb9czupn46.playlists
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `s3p5x7kb9czupn46`.`playlists` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `month` VARCHAR(45) NULL DEFAULT NULL,
  `year` YEAR NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `spotify_url` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_playlists_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_playlists_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `s3p5x7kb9czupn46`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8mb3;

-- ----------------------------------------------------------------------------
-- Table s3p5x7kb9czupn46.playlists_has_songs
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `s3p5x7kb9czupn46`.`playlists_has_songs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `playlist_id` INT NOT NULL,
  `song_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `playlists_has_songscol` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_playlists_has_songs_songs1_idx` (`song_id` ASC) VISIBLE,
  INDEX `fk_playlists_has_songs_playlists1_idx` (`playlist_id` ASC) VISIBLE,
  CONSTRAINT `fk_playlists_has_songs_playlists1`
    FOREIGN KEY (`playlist_id`)
    REFERENCES `s3p5x7kb9czupn46`.`playlists` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_playlists_has_songs_songs1`
    FOREIGN KEY (`song_id`)
    REFERENCES `s3p5x7kb9czupn46`.`songs` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 30
DEFAULT CHARACTER SET = utf8mb3;

-- ----------------------------------------------------------------------------
-- Table s3p5x7kb9czupn46.post_has_people
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `s3p5x7kb9czupn46`.`post_has_people` (
  `people_id` INT NOT NULL,
  `post_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`people_id`, `post_id`),
  INDEX `fk_people_has_posts_posts1_idx` (`post_id` ASC) VISIBLE,
  INDEX `fk_people_has_posts_people1_idx` (`people_id` ASC) VISIBLE,
  CONSTRAINT `fk_people_has_posts_people1`
    FOREIGN KEY (`people_id`)
    REFERENCES `s3p5x7kb9czupn46`.`people` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_people_has_posts_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `s3p5x7kb9czupn46`.`posts` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- ----------------------------------------------------------------------------
-- Table s3p5x7kb9czupn46.posts
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `s3p5x7kb9czupn46`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `category_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_featured` TINYINT NULL DEFAULT '0',
  `cover_picture` VARCHAR(255) NULL DEFAULT NULL,
  `synopsis` VARCHAR(255) NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  `content` LONGTEXT NULL DEFAULT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `is_public` TINYINT NULL DEFAULT '0',
  `posted_date` DATE NULL DEFAULT (curdate()),
  PRIMARY KEY (`id`),
  INDEX `fk_pages_has_categories_categories1_idx` (`category_id` ASC) VISIBLE,
  INDEX `fk_posts_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_pages_has_categories_categories1`
    FOREIGN KEY (`category_id`)
    REFERENCES `s3p5x7kb9czupn46`.`categories` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_posts_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `s3p5x7kb9czupn46`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 29
DEFAULT CHARACTER SET = utf8mb3;

-- ----------------------------------------------------------------------------
-- Table s3p5x7kb9czupn46.refit_pages
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `s3p5x7kb9czupn46`.`refit_pages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `news` TEXT NULL DEFAULT NULL,
  `schedule` TEXT NULL DEFAULT NULL,
  `loc` TEXT NULL DEFAULT NULL,
  `about_me` TEXT NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `playlist_id` INT NULL DEFAULT NULL,
  `banner1_picture` VARCHAR(255) NULL DEFAULT NULL,
  `banner2_picture` VARCHAR(255) NULL DEFAULT NULL,
  `about_me_picture` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_refit_page_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_refit_page_playlists1_idx` (`playlist_id` ASC) VISIBLE,
  CONSTRAINT `fk_refit_page_playlists1`
    FOREIGN KEY (`playlist_id`)
    REFERENCES `s3p5x7kb9czupn46`.`playlists` (`id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL,
  CONSTRAINT `fk_refit_page_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `s3p5x7kb9czupn46`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb3;

-- ----------------------------------------------------------------------------
-- Table s3p5x7kb9czupn46.songs
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `s3p5x7kb9czupn46`.`songs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `artist` VARCHAR(45) NULL DEFAULT NULL,
  `link` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_songs_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_songs_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `s3p5x7kb9czupn46`.`users` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB
AUTO_INCREMENT = 40
DEFAULT CHARACTER SET = utf8mb3;

-- ----------------------------------------------------------------------------
-- Table s3p5x7kb9czupn46.users
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `s3p5x7kb9czupn46`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `pw` CHAR(60) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_verified` TINYINT NULL DEFAULT '0',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb3;
SET FOREIGN_KEY_CHECKS = 1;

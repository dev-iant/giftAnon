-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema giftanon
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `giftanon` ;

-- -----------------------------------------------------
-- Schema giftanon
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `giftanon` DEFAULT CHARACTER SET utf8mb3 ;
-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema validateusers
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `validateusers` ;

-- -----------------------------------------------------
-- Schema validateusers
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `validateusers` ;
USE `giftanon` ;

-- -----------------------------------------------------
-- Table `giftanon`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `giftanon`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(150) NOT NULL,
  `role` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `giftanon`.`purchases`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `giftanon`.`purchases` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `item_name` VARCHAR(100) NOT NULL,
  `category` VARCHAR(45) NOT NULL,
  `facility` VARCHAR(75) NOT NULL,
  `city` VARCHAR(75) NOT NULL,
  `quantity` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `purchaser_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_purchases_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_purchases_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `giftanon`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

USE `validateusers` ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

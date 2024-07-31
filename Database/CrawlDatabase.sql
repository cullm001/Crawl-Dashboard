-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema crawlbee
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema crawlbee
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `crawlbee` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `crawlbee` ;

-- -----------------------------------------------------
-- Table `crawlbee`.`crawl_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `crawlbee`.`crawl_info` (
  `crawl_id` VARCHAR(45) NOT NULL,
  `cluster_id` VARCHAR(45) NULL DEFAULT NULL,
  `request_time` TIMESTAMP NULL DEFAULT NULL,
  `response_time` TIMESTAMP NULL DEFAULT NULL,
  `total_requests` INT NULL DEFAULT NULL,
  `requests_per_sec` INT NULL DEFAULT NULL,
  `concurrent_requests` INT NULL DEFAULT NULL,
  `estimated_time_to_complete` INT NULL DEFAULT NULL,
  `avg_cost_per_query` DECIMAL(5,2) NULL DEFAULT NULL,
  `api_status_code` INT NULL DEFAULT NULL,
  `success_rate` DECIMAL(4,2) NULL DEFAULT NULL,
  `error_rate` DECIMAL(4,2) NULL DEFAULT NULL,
  PRIMARY KEY (`crawl_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `crawlbee`.`node_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `crawlbee`.`node_info` (
  `time` TIMESTAMP NULL DEFAULT NULL,
  `node_id` VARCHAR(45) NOT NULL,
  `cpu_usage` DECIMAL(4,2) NULL DEFAULT NULL,
  `memory_usage` DECIMAL(4,2) NULL DEFAULT NULL,
  `bandwidth_usage` DECIMAL(4,2) NULL DEFAULT NULL,
  `diskspace_usage` DECIMAL(4,2) NULL DEFAULT NULL,
  PRIMARY KEY (`node_id`),
  INDEX `node_info_time_idx` (`time` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `crawlbee`.`crawl_node`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `crawlbee`.`crawl_node` (
  `crawl_id` VARCHAR(45) NOT NULL,
  `node_id` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`crawl_id`, `node_id`),
  INDEX `cn_node_id_idx` (`node_id` ASC) INVISIBLE,
  INDEX `cn_crawl_id_idx` (`crawl_id` ASC) VISIBLE,
  CONSTRAINT `cn_crawl_id`
    FOREIGN KEY (`crawl_id`)
    REFERENCES `crawlbee`.`crawl_info` (`crawl_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `cn_node_id`
    FOREIGN KEY (`node_id`)
    REFERENCES `crawlbee`.`node_info` (`node_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `crawlbee`.`request_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `crawlbee`.`request_info` (
  `time` TIMESTAMP NULL DEFAULT NULL,
  `request_id` VARCHAR(45) NOT NULL,
  `crawl_id` VARCHAR(45) NULL DEFAULT NULL,
  `proxy` VARCHAR(45) NULL DEFAULT NULL,
  `engine` VARCHAR(45) NULL DEFAULT NULL,
  `fingerprint` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`request_id`),
  INDEX `crawl_id_idx` (`crawl_id` ASC) VISIBLE,
  INDEX `request_time_idx` (`time` ASC) VISIBLE,
  CONSTRAINT `fk_req_info_crawl_id`
    FOREIGN KEY (`crawl_id`)
    REFERENCES `crawlbee`.`crawl_info` (`crawl_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `crawlbee`.`response_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `crawlbee`.`response_info` (
  `time` TIMESTAMP NULL DEFAULT NULL,
  `response_id` VARCHAR(45) NOT NULL,
  `request_id` VARCHAR(45) NULL,
  `domain_name` VARCHAR(45) NULL DEFAULT NULL,
  `website_status_code` INT NULL DEFAULT NULL,
  `is_blocked` BINARY(1) NULL DEFAULT NULL,
  `bytes_downloaded` INT NULL DEFAULT NULL,
  `download_speed` DECIMAL(5,2) NULL DEFAULT NULL,
  PRIMARY KEY (`response_id`),
  INDEX `fk_resp_info_req_id_idx` (`request_id` ASC) INVISIBLE,
  INDEX `resp_info_time_idx` (`time` ASC) VISIBLE,
  CONSTRAINT `fk_resp_info_req_id`
    FOREIGN KEY (`request_id`)
    REFERENCES `crawlbee`.`request_info` (`request_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

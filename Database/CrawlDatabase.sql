-- Set necessary variables

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- Create tables
CREATE TABLE `crawl_info` (
  `crawl_id` VARCHAR(45) NOT NULL,
  `cluster_id` VARCHAR(45) NULL DEFAULT NULL,
  `total_requests` INT NULL DEFAULT NULL,
  `requests_per_sec` INT NULL DEFAULT NULL,
  `concurrent_requests` INT NULL DEFAULT NULL,
  `cost` DECIMAL(5,2) NULL DEFAULT NULL,
  `domain_name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`crawl_id`),
  INDEX `cluster_id_idx` (`cluster_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


CREATE TABLE `node_info` (
  `time` TIMESTAMP NULL DEFAULT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  `node_id` VARCHAR(45) NULL DEFAULT NULL,
  `cpu_usage` DECIMAL(4,2) NULL DEFAULT NULL,
  `memory_usage` DECIMAL(4,2) NULL DEFAULT NULL,
  `bandwidth_usage` DECIMAL(4,2) NULL DEFAULT NULL,
  `diskspace_usage` DECIMAL(4,2) NULL DEFAULT NULL,
  `crawl_id` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `node_info_time_idx` (`time` ASC) VISIBLE,
  INDEX `node_id_idx` (`node_id` ASC) INVISIBLE,
  INDEX `fk_node_crawlid_idx` (`crawl_id` ASC) VISIBLE,
  CONSTRAINT `fk_node_crawlid`
    FOREIGN KEY (`crawl_id`)
    REFERENCES `crawl_info` (`crawl_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


CREATE TABLE `request_info` (
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
    REFERENCES `crawl_info` (`crawl_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


CREATE TABLE `response_info` (
  `time` TIMESTAMP NULL DEFAULT NULL,
  `response_id` VARCHAR(45) NOT NULL,
  `request_id` VARCHAR(45) NULL DEFAULT NULL,
  `crawl_id` VARCHAR(45) NULL DEFAULT NULL,
  `http_status_code` INT NULL DEFAULT NULL,
  `is_blocked` TINYINT(1) NULL DEFAULT NULL,
  `bytes_downloaded` INT NULL DEFAULT NULL,
  `download_speed` DECIMAL(5,2) NULL DEFAULT NULL,
  `response_time` DECIMAL(5,2) NULL DEFAULT NULL,
  PRIMARY KEY (`response_id`),
  INDEX `fk_resp_info_req_id_idx` (`request_id` ASC) INVISIBLE,
  INDEX `resp_info_time_idx` (`time` ASC) INVISIBLE,
  INDEX `fk_resp_info_crawlid_idx` (`crawl_id` ASC) VISIBLE,
  CONSTRAINT `fk_resp_info_crawl_id`
    FOREIGN KEY (`crawl_id`)
    REFERENCES `crawl_info` (`crawl_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_resp_info_req_id`
    FOREIGN KEY (`request_id`)
    REFERENCES `request_info` (`request_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- Restore variables to original state
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

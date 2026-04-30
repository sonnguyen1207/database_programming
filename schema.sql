-- Adminer 4.7.6 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `building`;
CREATE TABLE `building` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `use` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP VIEW IF EXISTS `building_electricity_cost_daily`;
CREATE TABLE `building_electricity_cost_daily` (`Building ID` int(11), `date` date, `price` decimal(10,2), `Use` double, `Cost Per Day` double);


DROP TABLE IF EXISTS `DATA`;
CREATE TABLE `DATA` (
  `id` tinyint(4) DEFAULT NULL,
  `property_id` tinyint(4) DEFAULT NULL,
  `timestamp` varchar(255) DEFAULT NULL,
  `reportingGroup` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `unit` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `electricity`;
CREATE TABLE `electricity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `property` bigint(20) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `value` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_property` (`property`),
  CONSTRAINT `fk_property` FOREIGN KEY (`property`) REFERENCES `properties` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP VIEW IF EXISTS `electricity_cost_FIN_2025`;
CREATE TABLE `electricity_cost_FIN_2025` (`country` varchar(100), `iso3_code` varchar(3), `date` date, `price` decimal(10,2));


DROP TABLE IF EXISTS `electricity_prices`;
CREATE TABLE `electricity_prices` (
  `country` varchar(100) NOT NULL,
  `iso3_code` varchar(3) NOT NULL,
  `date` date NOT NULL,
  `price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`iso3_code`,`date`),
  KEY `date` (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `measurements`;
CREATE TABLE `measurements` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `property_code` varchar(255) DEFAULT NULL,
  `value` float(10,4) DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `properties`;
CREATE TABLE `properties` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `code` varchar(100) DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `building_electricity_cost_daily`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `building_electricity_cost_daily` AS select `b`.`id` AS `Building ID`,`e`.`date` AS `date`,`e`.`price` AS `price`,`b`.`use` AS `Use`,`e`.`price` * `b`.`use` AS `Cost Per Day` from (`electricity_cost_FIN_2025` `e` join `building` `b` on(`b`.`date` = `e`.`date`));

DROP TABLE IF EXISTS `electricity_cost_FIN_2025`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `electricity_cost_FIN_2025` AS select `electricity_prices`.`country` AS `country`,`electricity_prices`.`iso3_code` AS `iso3_code`,`electricity_prices`.`date` AS `date`,`electricity_prices`.`price` AS `price` from `electricity_prices` where `electricity_prices`.`iso3_code` = 'FIN';

-- 2026-04-30 05:02:41
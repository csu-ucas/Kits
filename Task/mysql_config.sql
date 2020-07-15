DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks` (
  `taskId` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `containers` varchar(255) NOT NULL,
  `specifyNode` varchar(255) NOT NULL,
  `compType` varchar(255) NOT NULL,
  `compNum` int(4) NOT NULL,
  `compMemory` varchar(16) NOT NULL,
  `createTime` datetime(6) DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`taskId`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `tasks` WRITE;
insert into `tasks`(`name`,`containers`,`specifyNode`,`compType`,`compNum`,`compMemory`,`priority`) values('task1','[test3_alpine, test4_ubuntu]',1,'CPU',1,'100m',1);
UNLOCK TABLES;

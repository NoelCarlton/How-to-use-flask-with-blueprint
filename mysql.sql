DROP TABLE IF EXISTS user;

CREATE TABLE `user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` CHAR(15) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL COMMENT '用户名字',
  `telephone` CHAR(12) NOT NULL COMMENT '电话',
  `age` INT NOT NULL DEFAULT 0 COMMENT '年龄',
  UNIQUE INDEX `telephone_UNIQUE` (`telephone` ASC),
  PRIMARY KEY (`id`, `telephone`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = '用户信息，此处写出来纯粹是为了说明项目怎么使用sqlAchemy';
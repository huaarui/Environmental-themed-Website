/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80040 (8.0.40)
 Source Host           : localhost:3306
 Source Schema         : environmental_app

 Target Server Type    : MySQL
 Target Server Version : 80040 (8.0.40)
 File Encoding         : 65001

 Date: 27/05/2025 15:31:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for environmental_app_comment
-- ----------------------------
DROP TABLE IF EXISTS `environmental_app_comment`;
CREATE TABLE `environmental_app_comment`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `post_id` int NULL DEFAULT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `created_at` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of environmental_app_comment
-- ----------------------------
INSERT INTO `environmental_app_comment` VALUES (6, 8, '非常赞同楼主的观点！我也觉得环保要从自身做起，从点滴小事做起。我现在出门都会自带环保袋，尽量不使用一次性塑料袋，感觉自己也为环保做了一点贡献，很有成就感。', '2025-05-27 03:09:07');

-- ----------------------------
-- Table structure for environmental_app_forumpost
-- ----------------------------
DROP TABLE IF EXISTS `environmental_app_forumpost`;
CREATE TABLE `environmental_app_forumpost`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '评论id',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '评论标题',
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '评论',
  `created_at` datetime NULL DEFAULT NULL COMMENT '时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of environmental_app_forumpost
-- ----------------------------
INSERT INTO `environmental_app_forumpost` VALUES (8, '保护水土，从身边小事做起', '最近我发现我们身边的水土资源正面临着各种威胁，比如水土流失、水污染等等。其实，我们每个人都可以从身边的小事做起，为保护水土出一份力。比如，减少使用一次性塑料制品，做好垃圾分类，节约用水等等。这些看似微不足道的小事，积少成多，就能对我们的环境产生积极的影响。希望大家都能行动起来，一起守护我们的水土资源。', '2025-05-27 03:08:52');

SET FOREIGN_KEY_CHECKS = 1;

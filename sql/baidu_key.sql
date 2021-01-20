/*
 Navicat Premium Data Transfer

 Source Server         : SQLserver单位服务器
 Source Server Type    : SQL Server
 Source Server Version : 10506000
 Source Host           : 101.200.47.16:1433
 Source Catalog        : test
 Source Schema         : dbo

 Target Server Type    : SQL Server
 Target Server Version : 10506000
 File Encoding         : 65001

 Date: 13/01/2021 17:48:22
*/


-- ----------------------------
-- Table structure for baidu_key
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[baidu_key]') AND type IN ('U'))
	DROP TABLE [dbo].[baidu_key]
GO

CREATE TABLE [dbo].[baidu_key] (
  [id] int  NOT NULL,
  [api_key] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [secret_key] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[baidu_key] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of baidu_key
-- ----------------------------
INSERT INTO [dbo].[baidu_key] ([id], [api_key], [secret_key]) VALUES (N'1', N'r9c9Sef1T9wlxEnBMcfD6x1K', N'v4lIrtqonCNNstuKiFIlGoG08d0ixlwO')
GO


-- ----------------------------
-- Primary Key structure for table baidu_key
-- ----------------------------
ALTER TABLE [dbo].[baidu_key] ADD CONSTRAINT [PK__baidu_oc__3213E83F13F1F5EB] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


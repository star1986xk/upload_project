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

 Date: 13/01/2021 17:48:57
*/


-- ----------------------------
-- Table structure for update_file
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[update_file]') AND type IN ('U'))
	DROP TABLE [dbo].[update_file]
GO

CREATE TABLE [dbo].[update_file] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [uid] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user_id] int  NULL,
  [project_id] int  NULL,
  [ftp_id] int  NULL,
  [project_name] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [keyword] nvarchar(max) COLLATE Chinese_PRC_CI_AS  NULL,
  [is_wait] tinyint  NULL
)
GO

ALTER TABLE [dbo].[update_file] SET (LOCK_ESCALATION = TABLE)
GO

EXEC sp_addextendedproperty
'MS_Description', N'1:等待审核项目',
'SCHEMA', N'dbo',
'TABLE', N'update_file',
'COLUMN', N'is_wait'
GO


-- ----------------------------
-- Auto increment value for update_file
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[update_file]', RESEED, 5)
GO


-- ----------------------------
-- Uniques structure for table update_file
-- ----------------------------
ALTER TABLE [dbo].[update_file] ADD CONSTRAINT [UQ__update_f__DD7012657FEAFD3E] UNIQUE NONCLUSTERED ([uid] ASC)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Primary Key structure for table update_file
-- ----------------------------
ALTER TABLE [dbo].[update_file] ADD CONSTRAINT [PK__update_f__3213E83F7D0E9093] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


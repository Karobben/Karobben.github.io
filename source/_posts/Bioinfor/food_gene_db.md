---
title: "Build A Personal BioDatabase with Mysql"
description: "Build A Personal BioDatabase with Mysql, an example of diets and gene interaction database"
date: 2021/01/31
url: food_gene_db
toc: true
excerpt: "Build A Personal BioDatabase with Mysql, an example of diets and gene interaction database"
tags: [Database, Mysql]
category: [Biology, Database]
cover: 'https://s1.ax1x.com/2020/07/27/aFEKqH.png'
thumbnail:  'https://s1.ax1x.com/2020/07/27/aFEKqH.png'
priority: 10000
covercopy: '© Karobben'
---

## Build A Personal BioDatabase with Mysql

This is my first time to try build a Database on my own.
I'm recording my experience and the structure of this database here in order to prevent me from forgetting how to retrieve or update the data in it.

Before doing this, I spend a few hours to taught myself about Mysql and recorded all my notes at [blog](https://karobben.github.io/2021/01/31/Linux/mysql)
Please feel free to check the Mysql grammar before running codes below if you are an newbies like me.

I'll start to do this with few questions:
- Why I'd like to build a database
- What I database I'd like to have
- Which features does this DB will have

## Why and What
Generally, I am writing a paper about the diet-switch experiment which has a few RNA-seq data-set.
It could give me a great help if there is a database which targeted to the diet-gene interaction.
But, I can't find a one.
Though, I know that gene regulated by nutrition effect could mostly contributed to of the effects like immune system depress, stress response, etc. But it do help researches focusing the interactions they may interested rather than searching blindly among more than 20 thousands of genes from RNA-seq or other high-throughput results.
So, I decided to write a database which target to the how the genes responded to nutrition effects.

Due to the limited of the experience and capability, I'll store the well verified and reliable data, WB and qPCR for instance, only and maybe I'll considerate the NGS data in the feature. It could be very fun to deal with large quantity of data, you know, as a user, definitely not a manager.

## Which

At present, I think there are few separate tables I'd like to have
- Species (KEGG Organisms: has (I just like this elegant abstract))
- Species Taxonomy (A complex-version like NCBI taxonomy or sample version like KEGG Organisms?)
- Gene Annotation (I'll try, at least.)
  - Other IDs
  - GO entry
  - Kegg ID
  - Kegg map
- Food entities (not too much experience about that. But the name will basically based on the paper)
- Regulation Net

## Gene Annotation table
This is one of the most important table since the clarity of entities is pretty important for gene-related database since a common gene could have to many names.

### Gene Annotation
At present, I'd like the gene has the entities like below: (mostly contributed by uniprot database)
- UniProtID:      P04637
- UniprotName:    P53_HUMAN
- Gene name:      P53
- Organism:       Homo sapiens (Human)
- Function:       Acts as a tumor suppressor in many tumor type...
- GO-Molecular-function: ATP binding;chaperone binding...
- GO-Biological-process: autophagy;B cell lineage commitment
- KEGG:           hsa7157 (https://www.genome.jp/dbget-bin/www_bget?hsa:7157)
- KEGG maps:      hsa01522;hsa01524;hsa04010...

## Diet protocol
- Diet id
- Diet name
- Diet Protocol
- Citation

### Regulation
- Diet id
- Diet_secular (Soy protein)
- Diet_specific ()
- Diet_SN ()
- Specious
- Specious_muta
- Genes
- Ratio (up/down)
- Experiment (WB/qPCR/NGS)


## Codes

## Create DB
```sql
CREATE DATABASE IF NOT EXISTS `fgidb`;
USE fgidb;

-- Create a table
CREATE TABLE regulation_net(
  Diet_id INT NOT NULL AUTO_INCREMENT,
  Diet_secular VARCHAR(100),
  Diet_specific VARCHAR(100),
  Diet_SN VARCHAR(100),
  Specious VARCHAR(100),
  Organs VARCHAR(100),
  Specious_muta VARCHAR(100),
  Morphology VARCHAR(1000),
  Genes VARCHAR(100),
  Ratio VARCHAR(100),
  Validation VARCHAR(100),
  Citation VARCHAR(1000),
  submission_date  VARCHAR(1000),
  PRIMARY KEY ( Diet_id )
  )ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO regulation_net
  (Diet_secular, Specious,Specious_muta, Genes, Morphology, submission_date
  )
  VALUES
  ("Fish Oil", 'mmu', 'C57BL/6J Mice', 'CPT1A_MOUSE', 'Upregulates Intestinal Lipid Metabolism; Reduces Body Weight Gain' , NOW());

SELECT * from regulation_net WHERE Diet_id=1;


UPDATE regulation_net SET Citation='Dietary Fish Oil Upregulates Intestinal Lipid Metabolism and Reduces Body Weight Gain in C57BL/6J Mice' WHERE Diet_id=1;
```

## INPUT and OUTPUT
### Input
```sql
-- insert and replace

DROP TABLE regulation_tmp;
CREATE TABLE regulation_tmp(
  Diet_id INT NOT NULL AUTO_INCREMENT,
  Diet_secular VARCHAR(100),
  Diet_specific VARCHAR(100),
  Diet_SN VARCHAR(100),
  Specious VARCHAR(100),
  Specious_muta VARCHAR(100),
  Morphology VARCHAR(1000),
  Genes VARCHAR(100),
  Ratio VARCHAR(100),
  Validation VARCHAR(100),
  Citation VARCHAR(1000),
  subm VARCHAR(100),
  PRIMARY KEY ( Diet_id )
  )ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA INFILE '/var/lib/mysql-files/regulation_net.csv' REPLACE
INTO TABLE regulation_net
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';


SELECT * FROM regulation_net
UNION ALL
SELECT * FROM regulation_tmp
ORDER BY Diet_id;

```

### output

```sql
-- output as csv
SELECT * FROM regulation_net;


SELECT * INTO OUTFILE '/var/lib/mysql-files/regulation_net.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM regulation_net;
```

# Introduction

A platform that helps users highlight or delete duplicate contents of an excel file

## Project Name

excel_comp

### Unique name

exccomp

## Logo

![This is a alt text.](/image/sample.png "This is a sample image.")

## Goal

### Problem Statement
Highlighting or removing duplicates in an excel/csv file can prove difficult for users that do not know their way around using excel and/or writing VBA (Visual Basic for Applications) code.

The duplicate highlight feature works well when applied on a single column in an excel file but doesn't do so well when multiple columns are selected. 

#### Example
|            | Column A   | Column B   |
| ---------- |:----------:|:----------:|
| **Row 1**  | Simon      | McCowell   |
| **Row 2**  | Janet      | Simon      |
| **Row 3**  | Precious   | Nova       |

In the example above, excel highlights the _'Simon'_ in Column A_Row 1 and Column B_Row 2, which should not be so.
A user expects that a name appearing in a column should not be considered a duplicate in another column.

### Our proposed Solution

To highlight or remove duplicates across multiple columns; while handling each column separately, on uploaded excel/csv files.

## Primary Feature

1. User: Unauthenticated
    * Visit the platform to view basic information about it
    * View and Interact with the documentation
    * Register to view more details
    * No access to use until registered

1. User: Authenticated
    * Full access to the platform
    * Allow upload csv/excel file
    * Users should get the option to:
    * Highlight duplicates in a single file
    * Remove duplicates and return a single file
    * Remove duplicates and return 2 files
    * Highlight duplicates and return 2 files
    * Show usage example to users
    * Allow user save data and come back to download

## Proposed Features
1. The user will be able to specify if operation should be performed with 'Case Sensivity'
1.  Allow the user upload more than one file; to compare their contents against each other

## Tools, languages, etc.
* Django (python)
* Figma
* HTML
* CSS
* JavaScript

## Links
1. View our [Figma Design](https://)
1. See our [Design Documentation](https://slite.com/organization/join-link/okeogheneonobraekpeyan/e0fDCHxEouZAvG6YxkLWD7/default)

###### Zuri Team Inc | I4G x Zuri Project Phase

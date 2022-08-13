# Introduction

A platform that helps users highlight or delete duplicate contents of an excel file

## Project Name

excel_comp

### Unique name

exccomp

## Logo

![exccomp logo](./excel_comp/homepage/static/images/Logo2.svg "Unique exccomp logo.")

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
1. View our [Figma Design](https://www.figma.com/file/HTwo1y7ypEGFKyU5bg4ysm/Team---103-Project?node-id=1%3A3)
1. See our [Design Documentation](https://slite.com/organization/join-link/okeogheneonobraekpeyan/e0fDCHxEouZAvG6YxkLWD7/default)

## Architecture we're using 
* Monolith (Django Templating)
* 

## File structure
_This shows what each folder is_

1. about_us - this is a django app in the project, containing everything that renders/serves the about page
1. accounts - this is a django app that renders the login/signup page and also contains the authentication codes
1. compare - this is another django app that renders the compare page
1. contact_page - this is another django app that renders the contact us page
1. excel_comp -  this is the root django project containing all the settings for the project
1. homepage - this is a django app containing the static files (css, images, js), landing page (home.html)

###### Zuri Team Inc | I4G x Zuri Project Phase

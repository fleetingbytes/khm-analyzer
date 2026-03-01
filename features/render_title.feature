Feature: Render Title

    Background:
        Given source documents in directory khm-sources

        Scenario Outline: Render Number
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the number of the tale
            Then the output is <output>

            Examples:
                | tale | edition | volume | output |
                | 1    | 1       | 1      | 1      |
                | 30   | 1       | 1      | 30     |
                #  Tale number 31 is wrongly printed as 30. So it was transcribed and annotated as 30
                | 31   | 1       | 1      | 30     |
                # Add more later when CI goes full live and we download all source files

        Scenario Outline: Render Title
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the title of the tale
            Then the output is <output>

            Examples:
                | tale | edition | volume | output                          |
                | 2    | 1       | 1      | Katz und Maus in Gesellschaft   |
                | 12   | 1       | 1      | Rapunzel                        |
                | 52   | 1       | 1      | König Droßelbart                |
                | 53   | 1       | 1      | Schneewittchen (Schneeweißchen) |
                | 30   | 1       | 1      | Läuschen und Flöhchen           |
                | 31   | 1       | 1      | Mädchen ohne Hände              |
                # Add more later when CI goes full live and we download all source files

        Scenario Outline: Render Head
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the head of the tale
            Then the output is <output>

            Examples:
                | tale | edition | volume | output                              |
                | 2    | 1       | 1      | 2. Katz und Maus in Gesellschaft    |
                | 12   | 1       | 1      | 12. Rapunzel                        |
                | 52   | 1       | 1      | 52. König Droßelbart                |
                | 53   | 1       | 1      | 53. Schneewittchen (Schneeweißchen) |
                | 30   | 1       | 1      | 30. Läuschen und Flöhchen           |
                #  Tale number 31 is wrongly printed as 30. So it was transcribed and annotated as 30
                | 31   | 1       | 1      | 30. Mädchen ohne Hände              |
                # Add more later when CI goes full live and we download all source files

### Summary of the Talk: Attacking Plagiarism Detectors

#### 1. **Problem Statement** 🛠️
- Plagiarism in computer science assignments is a prevalent issue in universities.
- Manual inspection of assignments is impractical due to high student-to-TA ratios and increased CS enrollment.
- Heavy reliance on plagiarism detection tools (e.g., Moss, JPLAG, Sherlock) to identify cheating.
- ![image](https://github.com/user-attachments/assets/bfa2138f-b3a0-4c0f-805c-0a790994aaf9)
- ![image](https://github.com/user-attachments/assets/abab8a32-f45c-4d54-8088-2034f9fb36b5)
- ![image](https://github.com/user-attachments/assets/ee89e9bd-0aea-4a03-b8f0-607470b7e180)
- ![image](https://github.com/user-attachments/assets/37d1fd38-d0b6-4399-8a79-3c06997406a3)

#### 2. **How Plagiarism Detectors Work** 🖥️
- **Normalization**: Code is preprocessed by renaming identifiers, removing comments, and formatting.
  ![image](https://github.com/user-attachments/assets/8157fc29-b054-4d18-b47f-5d015b3ed792)

- **Tokenization and Fingerprinting**:
  - Code is tokenized and converted into a set of fingerprints (e.g., n-grams, string tiling, or hash-based methods).
  - Tools compare fingerprints to assign similarity scores.
- Moss features:
  - Highlights similar lines using color.
  - Detects typical plagiarism techniques like identifier renaming, comment addition/removal, and code rearrangement.
    ![image](https://github.com/user-attachments/assets/1140ff45-a180-4f9d-b5d5-d50694b6f46e)
    ![image](https://github.com/user-attachments/assets/e6bf342d-ddbe-4aa0-b42a-b23022ac048b)
    ![image](https://github.com/user-attachments/assets/6d065415-6d22-4720-ba99-a1fdc2fc2475)
    ![image](https://github.com/user-attachments/assets/7a88bdc1-9c54-450e-9c03-d2a8d256a4a7)
    ![image](https://github.com/user-attachments/assets/a3b4190b-e879-4d10-8015-0d4c72fd3352)
    ![image](https://github.com/user-attachments/assets/289e645c-d26c-4b83-9f91-90fb08071a79)
    ![image](https://github.com/user-attachments/assets/a089480f-eb29-4117-a321-bbf124aa6520)
    ![image](https://github.com/user-attachments/assets/4894981e-00b8-4a37-926b-0ee5e757d8fa)
    ![image](https://github.com/user-attachments/assets/afb6f1c8-7145-4827-b60a-2005b6dff93b)
    ![image](https://github.com/user-attachments/assets/69ad84af-0ce6-4354-b294-9b1ffc980025)
    ![image](https://github.com/user-attachments/assets/755ad361-4574-4da6-9f76-dfab48f8fb10)
    ![image](https://github.com/user-attachments/assets/64f4d08d-8674-42d4-bcba-1d3f47359a03)
    ![image](https://github.com/user-attachments/assets/ad49ba02-7bec-4fa7-b961-d79da2ced496)
    ![image](https://github.com/user-attachments/assets/37cf9ce6-971b-4e41-acaf-c96ae55df167)

#### 3. **The MOSSAD System** 🚨
- **Purpose**: Enables students to bypass plagiarism detection tools.
- **Capabilities**:
  - Generates semantically equivalent variants of code with near-zero similarity scores.
  - Produces multiple distinct variants from a single source file.
  - Effective across all tested plagiarism detectors.

#### 4. **Core Techniques of MOSSAD** 🔧
- **Fingerprint Disruption**: Modifies code to ensure fingerprints do not collide.
  - Example: Inserts variable declarations or existing code snippets in innocuous ways.
- **Semantic Preservation**: Ensures all modifications retain the original program’s functionality.
  - Verifies equivalence using compilation and optimization checks.

#### 5. **Research Findings** 📊
- **Effectiveness**:
  - 100% of MOSSAD files scored below the average authentic similarity score.
  - Enables mass plagiarism with low inter-variant similarity (≤25%).
- **TA Spot Checks**:
  - TAs failed to detect MOSSAD-modified files as suspicious.
  - MOSSAD code had comparable readability and design scores to authentic code.
- **Cross-Tool Testing**: MOSSAD bypassed all tested plagiarism detectors.

#### 6. **Partial Countermeasures** 🛡️
- **Compile to Assembly**: Compare assembly outputs instead of source code; increases similarity scores to ~80%.
- **Pedagogical Changes**:
  - Integrate GitHub to monitor commits.
  - Use code reviews to assess student understanding.

#### 7. **Conclusion** 📌
- **Plagiarism Detectors' Flaws**:
  - Focus on syntactic features rather than semantic equivalence.
  - Vulnerable to systematic attacks like MOSSAD.
- **Call to Action**:
  - Re-evaluate reliance on current tools.
  - Invest in advanced, semantic-based detection methods.
  - Enhance academic integrity through better pedagogical practices.


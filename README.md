Explanation of testFile.txt:
1. "VX.VY.(X->X->X)->(Y)->X"
  Tests for an uninhabited type.
2. "VX.VY.(X->X->Y)->Y"
  Tests for an uninhabited type.
3. "VX.VY.(X->X->Y)->(X)->Y"
  Tests for type inhabited by one term
4. "VX.VY.(X->X->Y)->(X)->(X)->Y"
  Tests for a type inhabited by four terms.
5. "VX.(X->X->X)->(X)->X"
  Test for infinite type.
6. "VX.VY.VZ.(X->X->Z)->(Y->X)->(Y)->Z"
  Test for type that relies on variable that must be generated by genTerms. One Term.
7. "VX.VY.VZ.(X->X->Z)->(Y->X)->(Y)->(X)->Z"
  Test for a type inhabited by four terms, but one of the substituting terms must be created in genTerms.
8. "VX.VY(X->X->X)->(Y->X)->(Y)->X"
  Test for infinite type that has terms created in genTerms.
9. "VX.VY.VZ.VR.(X->X->Z)->(R->X)->(Y->R)->(Y->R)->(Y)->Z"
  Test for multiple ways term can be constructed in genTerms. Four Terms
10. "VX.VY.VR.VQ.(X->X->Q)->(R->X)->(Y->R)->(Y)->(Y)->Q"
  Test for multiple ways term can be constructed in genTerms. Four terms.
11. "VX.VY.VR.VQ.(X->X->Q)->(R->X)->(Y->R)->(Y->R)->(Y)->(Y)->Q"
  Test for multiple ways term can be constructed in genTerms. Sixteen terms.
12. "VX.VY.VZ.(X->X->X)->(X)->Z"
  Test for type uninhabited because first term does not result in final term.

Note: Type must be wrapped in quotes, no spaces
      All types except for the final type must be wrapped in parentheses
      No parentheses can be contained in types
      Final type should only be one term (no arrows)
      Type variables cannot be numbers

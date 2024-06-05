import torch  # allows Tensor computation with strong GPU acceleration
from transformers import pipeline  # fast way to use pre-trained models for inference


def prompt_dolly_3b(prompt):

    # define helper function
    def get_completion_dolly(str_input):
        system = f"""
    You are an expert Physicist.
    You are good at explaining Physics concepts in simple words.
    Help as much as you can. you know the following formulas: Average Speed Formula S = d/t
Acceleration Formula  a =v-u/t
Density Formula   P=m/V
Power Formula P=W/t
Newton’s Second Law F = m × a
Weight Formula  W=mg
Pressure Formula  P=F/A
Ohm’s Law Formula V= I × R
Kinetic Energy Formula  E = ½ mv²
Frequency Formula F =v/λ
Pendulum Formula  T = 2π√L/g
Fahrenheit Formula  F = (9/5× °C) + 32
Work Formula  W = F × d × cosθ
Torque Formula  T = F × r × sinθ
Displacement Formula  ΔX = Xf–Xi 
Mass Formula  F = m × a or m = F/m
Amplitude Formula x = A sin (ωt + ϕ)  
Tension Formula T= mg+ma
Surface Charge Density Formula  σ = q / A
Linear Speed Formula  V(linear speed) = ΔS/ΔT
Position Formula  Δx=x2−x1
Heat of Fusion Formula  q = m × ΔHF
Gravity Formula F α m₁m₂/r₂
Spring Potential Energy Formula P.E=1/2 k × x2
Physics Kinematics Formula  v2=v2o+2a(x-xo)
DC Voltage Drop Formula V=I ×  R
Hubble’s Law Formula  v = Ho r
Induced Voltage Formula e = – N(dΦB/dt)
Latent Heat Formula L = Q / M
Wavelength Formula  λ = v/f
Gravitational Force Formula F = G(m1m2)/R2
Potential Energy Formula  PE = mgh
Strain Energy Formula U = Fδ / 2
Friction Force Formula  f = μN
Cell Potential Formula  E0cell = E0red − E0oxid
Shear Modulus Formula (shear stress)/(shear strain) = (F/A)/(x/y) 
Water Pressure Formula  Water pressure= ρ g h
Refractive Index Formula  n = c/v
Centroid Formula  C = [(x1 + x2 + x3)/ 3, (y1 + y2 + y3)/ 3].
you know:
addition: Addition (usually signified by the plus symbol +) is one of the four basic operations of arithmetic, the other three being subtraction, multiplication and division.[2] The addition of two whole numbers results in the total amount or sum of those values combined. The example in the adjacent image shows two columns of three apples and two apples each, totaling at five apples. This observation is equivalent to the mathematical expression "3 + 2 = 5" (that is, "3 plus 2 is equal to 5").
subtraction: Subtraction (which is signified by the minus sign −) is one of the four arithmetic operations along with addition, multiplication and division. Subtraction is an operation that represents removal of objects from a collection.[1] For example, in the adjacent picture, there are 5 − 2 peaches—meaning 5 peaches with 2 taken away, resulting in a total of 3 peaches. Therefore, the difference of 5 and 2 is 3; that is, 5 − 2 = 3. While primarily associated with natural numbers in arithmetic, subtraction can also represent removing or decreasing physical and abstract quantities using different kinds of objects including negative numbers, fractions, irrational numbers, vectors, decimals, functions, and matrices.[2]
In a sense, subtraction is the inverse of addition. That is, c = a − b if and only if c + b = a. In words: the difference of two numbers is the number that gives the first one when added to the second one.
Subtraction follows several important patterns. It is anticommutative, meaning that changing the order changes the sign of the answer. It is also not associative, meaning that when one subtracts more than two numbers, the order in which subtraction is performed matters. Because 0 is the additive identity, subtraction of it does not change a number. Subtraction also obeys predictable rules concerning related operations, such as addition and multiplication. All of these rules can be proven, starting with the subtraction of integers and generalizing up through the real numbers and beyond. General binary operations that follow these patterns are studied in abstract algebra.
multiplication: The multiplication of whole numbers may be thought of as repeated addition; that is, the multiplication of two numbers is equivalent to adding as many copies of one of them, the multiplicand, as the quantity of the other one, the multiplier; both numbers can be referred to as factors.
division: At an elementary level the division of two natural numbers is, among other possible interpretations, the process of calculating the number of times one number is contained within another.[1]: 7  For example, if 20 apples are divided evenly between 4 people, everyone receives 5 apples (see picture). However, this number of times or the number contained (divisor) need not be integers.
Negative numbers: In mathematics, a negative number represents an opposite.[1] In the real number system, a negative number is a number that is less than zero. Negative numbers are often used to represent the magnitude of a loss or deficiency. A debt that is owed may be thought of as a negative asset. If a quantity, such as the charge on an electron, may have either of two opposite senses, then one may choose to distinguish between those senses—perhaps arbitrarily—as positive and negative. Negative numbers are used to describe values on a scale that goes below zero, such as the Celsius and Fahrenheit scales for temperature. The laws of arithmetic for negative numbers ensure that the common-sense idea of an opposite is reflected in arithmetic. For example, − (−3) = 3 because the opposite of an opposite is the original value.

Negative numbers are usually written with a minus sign in front. For example, −3 represents a negative quantity with a magnitude of three, and is pronounced "minus three" or "negative three". To help tell the difference between a subtraction operation and a negative number, occasionally the negative sign is placed slightly higher than the minus sign (as a superscript). Conversely, a number that is greater than zero is called positive; zero is usually (but not always) thought of as neither positive nor negative.[2] The positivity of a number may be emphasized by placing a plus sign before it, e.g. +3. In general, the negativity or positivity of a number is referred to as its sign.
        """
        prompt = f"#### System: {system}\n#### User: \n{str_input}\n\n#### Response from Dolly-v2-3b:"
        #print(prompt)
        dolly_response = dolly_pipeline(prompt, max_new_tokens=500)
        return dolly_response[0]["generated_text"]

    dolly_pipeline = dolly_pipeline = pipeline(
        model="databricks/dolly-v2-3b",
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
    )
    # let's prompt
    # prompt = "Why is the Sky blue?"
    print("-"*40+" DOLLY 3B "+"-"*40)
    response = get_completion_dolly(prompt)
    print("-" * 40 + "\nprompt: " + prompt)
    print("response: " + response + "\n" + "-" * 40)
    return response

// For each property K in T:
// If the property's type (T[K]) extends Function, set its type to the property's name (K)
// Else, set its type to `never`
type MapPropertiesToTheirNamesUnlessNonFunctions<T> = { [K in keyof T]: T[K] extends Function ? K : never };
type FunctionPropertyNames<T> = MapPropertiesToTheirNamesUnlessNonFunctions<T>[keyof T];
interface Part {
	id: number;
	name: string;
	subparts: Part[];
	updatePart(newName: string): void;
}
interface AnotherPart extends Part {
	shtroodle: Function
}
type Mapped = MapPropertiesToTheirNamesUnlessNonFunctions<Part>;
type MappedHardCoded = {
	id: never;
	name: never;
	subparts: never;
	updatePart: "updatePart"
}
type T40 = FunctionPropertyNames<Part>;  // "updatePart"
type T40HardCoded0 = MappedHardCoded["id" | "name" | "subparts" | "updatePart"];  // "updatePart"
type T40HardCoded1 = MappedHardCoded[keyof MappedHardCoded];  // "updatePart"

type CubicBezierFunction = [number, number, number, number];
type Jumpterm = 'jump-start' | 'jump-end' | 'jump-none' | 'jump-both' | 'start' | 'end';

/**Displays an animation iteration along n stops along the transition, displaying each stop for equal lengths of time.
 * For example, if n is 5,  there are 5 steps.
 * Whether the animation holds temporarily at 0%, 20%, 40%, 60% and 80%, on the 20%, 40%, 60%, 80% and 100%, or makes 5 stops between the 0% and 100% along the animation, or makes 5 stops including the 0% and 100% marks (on the 0%, 25%, 50%, 75%, and 100%) depends on which of the following jump terms is used*/
type StepsFunction = [number, Jumpterm];
type AnimationTimingFunction =
    'linear'
    | 'ease'
    | 'ease-in'
    | 'ease-out'
    | 'ease-in-out'
    | 'step-start'
    | 'step-end'
    | StepsFunction
    | CubicBezierFunction
type AnimationDirection = 'normal' | 'reverse' | 'alternate' | 'alternate-reverse';
type AnimationFillMode = 'none' | 'forwards' | 'backwards' | 'both';

interface CssOptions extends Omit<Partial<CSSStyleDeclaration>, keyof CssOptions>{
    animationDirection: AnimationDirection;
    animationFillMode: AnimationFillMode;
    animationIterationCount: number;
    animationPlayState: AnimationPlayState;
    animationTimingFunction: AnimationTimingFunction;
    padding: string | number;
    paddingBottom: string | number;
    paddingLeft: string | number;
    paddingRight: string | number;
    paddingTop: string | number;
    preload: "auto" | string;
    width: string | number;
}

function [bestEpsilon bestF1] = selectThreshold(yval, pval)
%SELECTTHRESHOLD Find the best threshold (epsilon) to use for selecting
%outliers
%   [bestEpsilon bestF1] = SELECTTHRESHOLD(yval, pval) finds the best
%   threshold to use for selecting outliers based on the results from a
%   validation set (pval) and the ground truth (yval).
%
%bestEpsilon bestF1] = SELECTTHRESHOLD(yval, pval)
%は、検証セット(pval)と基底真理(yval)からの結果に基づいて外れ値を選択するために
%使用する最良のしきい値を見つけます。

bestEpsilon = 0;
bestF1 = 0;
F1 = 0;

stepsize = (max(pval) - min(pval)) / 1000;
for epsilon = min(pval):stepsize:max(pval)
    
    % ====================== YOUR CODE HERE ======================
    % Instructions: Compute the F1 score of choosing epsilon as the
    %               threshold and place the value in F1. The code at the
    %               end of the loop will compare the F1 score for this
    %               choice of epsilon and set it to be the best epsilon if
    %               it is better than the current choice of epsilon.
    %指示。閾値としてイプシロンを選択した場合のF1スコアを計算し、その値をF1に配置します。
    %ループの最後のコードは、この選択されたイプシロンのF1スコアを比較し、
    %現在の選択されたイプシロンよりも優れている場合は、それを最高のイプシロンに設定します。      
    %               
    % Note: You can use predictions = (pval < epsilon) to get a binary vector
    %       of 0's and 1's of the outlier predictions
    %注意: predictions = (pval < epsilon)を使用して、
    %外れ値予測の0と1のバイナリベクトルを得ることができます。
    predictions = (pval < epsilon);
    tp = sum((predictions == 1) & (yval == 1));
    fp = sum((predictions == 1) & (yval == 0));
    fn = sum((predictions == 0) & (yval == 1));
    prec = tp /(tp+fp);
    rec  = tp /(tp+fn);
    F1 = 2 * prec * rec / (prec + rec);









    % =============================================================

    if F1 > bestF1
       bestF1 = F1;
       bestEpsilon = epsilon;
    end
end

end
